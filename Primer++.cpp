// Primer++
// github.com/smcclennon/Primer

// Started porting Primer.py on the 5th may 2020
// Finished recoding in C++ on the 7th may 2020



#include <string>
#include <iostream>
#include <fstream>
#include <ctime>
#include <map>
#include "Primer++.h" // Get the version number (aids with automatic building)
#include "json.hpp"

// OS specific features
#ifdef _WIN32
    #include "windows.h"
#elif defined(__APPLE__) || defined(__linux__)
    #include <unistd.h>
    bool linux = false;
#endif


using std::cout;
using std::endl;
using std::string;
using json = nlohmann::json;

string ver = primer_ver();
string proj = "Primer++";
string latest_prime_commas;

// Initialise/Define variable and function types
bool invalid = false;
bool console_update = false;
bool new_round = true;
unsigned long long round_calculations = 0;  // Calculations taken to find the current latest prime
int debug = 0;
double task_duration = 0;
#ifdef _WIN32
    double previous_task_duration;
#endif
std::clock_t task_start;

json json_config;
std::ofstream config_file;
std::ofstream txt_file_append;

unsigned long long latest_prime();
unsigned long long primes_found();
unsigned long long total_calculations();
string insert_commas(unsigned long long);
void windows_console_title(string);



// Allow the largest possible positive integer to be stored (max: 18,446,744,073,709,551,615 *or greater)
// * the actual value depends on the particular system and library implementation, but shall reflect the limits of these types in the target platform.
// https://www.cplusplus.com/reference/climits/
unsigned long long latest_prime() { return json_config["statistics"]["Latest Prime"].get<unsigned long long>(); }
unsigned long long primes_found() { return json_config["statistics"]["Primes Found"].get<unsigned long long>(); }
unsigned long long total_calculations() { return json_config["statistics"]["Total Calculations"].get<unsigned long long>(); }

// Format numbers with commas (1234567 -> 1,234,567)
// https://stackoverflow.com/a/24192835 // insert commas
string insert_commas(unsigned long long num)
{
    string numWithCommas = std::to_string(num);
    try {
        unsigned int insertPosition = numWithCommas.length() - 3;
        while (insertPosition > 0)
        {
            numWithCommas.insert(insertPosition, ",");
            insertPosition -= 3;
        }
    } catch (std::out_of_range &exc) {}
    return numWithCommas;
}

void windows_console_title(string title) {
    system(("title " + proj + " " + ver + title).c_str());
}

int main()
{
    if (debug >= 1) { proj += " [DEBUG: " + std::to_string(debug) + "]"; }
    #ifdef _WIN32
    windows_console_title("");
    #endif
    cout << proj << " " << ver << "   "
         << "A prime number generator\n"
         << "github.com/smcclennon/Primer\n"
         << "\nRewritten from the ground up in C++ (5th - 7th may 2020)\n"
         << "Various stability and performance improvements over the Python version\n"
         << "\n**This software is still under early development. Features and functionality are subject to change**\n"
         << std::flush;

    #ifdef _WIN32
        Sleep(3000);
    #elif defined(__APPLE__) || defined(__linux__)
        sleep(3);
    #endif

    cout << endl << endl;



    try {
        if (debug >= 2) { cout << "Trying to load config" << endl;
        }
        std::ifstream config_file_read("Primer_config.json");
        json_config = json::parse(config_file_read);
    } catch (nlohmann::detail::parse_error &exc) {
        cout << "Created Primer_config.json" << endl << endl;
        json_config = "{\"statistics\": {\"Total Calculations\": 0, \"Primes Found\": 0, \"Latest Prime\": 0}, \"debugging\": {\"Force Unix\": \"False\"}}"_json;
    }

    // Convert value types to unsigned long long
    json_config["statistics"]["Total Calculations"] = total_calculations();
    json_config["statistics"]["Latest Prime"] = latest_prime();
    json_config["statistics"]["Primes Found"] = primes_found();
    if (primes_found() > 0) { json_config["statistics"]["Latest Prime"] = latest_prime() + 1; }




    while (true)
    {
        if (new_round)
        {
            // https://stackoverflow.com/a/3220503
            task_start = std::clock();
            new_round = false;
        }


        if (debug >= 2) { cout << "\n-- RESTART WHILE TRUE --" << endl
                          << json_config.dump(4) << endl;
        }

        while (invalid == false)
        {

            if (debug >= 2) {
                cout << "[WHILE] Invalid: false" << endl
                << "[WHILE] latest_prime = " << latest_prime() << endl
                //<< "[WHILE] latest_prime % 2 == 0: ???" << endl
                << "[WHILE] Calculations = " << round_calculations << endl
                << "[WHILE] Total  = " << total_calculations() << endl
                << "--START IF--" << endl;

            }


            if (latest_prime() % 2 == 0) // If even
            {
                if (debug >= 2) { cout << "latest_prime % 2 == 0: True" << endl;
                }
                round_calculations++;
                if (debug >= 2) { cout << "[IF] Number is even" << endl;
                }
                invalid = true;
                if (debug >= 2) { cout << "[IF] Invalid: true" << endl;
                }
                break;
                if (debug >= 2) { cout << "[IF] Failed to break" << endl;
                }
            }

            if (debug >= 2) {
                cout << "--END IF--"
                << "\nCalculations = " << round_calculations
                << "\nTotal calculations = " << total_calculations()
                << "\n--START FOR LOOP--" << endl;
            }


            for (unsigned int i = 3; i < latest_prime(); i+=2)
            {
                round_calculations++;
                if (latest_prime() % i == 0)
                {
                    round_calculations++;
                    if (debug >= 2) { cout << "[FOR] Number is divisible\n[FOR] Invalid: true" << endl;
                    }
                    invalid = true;
                    //break;
                    if (debug >= 2) { cout << "[FOR] Failed to break" << endl;
                    }
                }
            }
            if (debug >= 2) {
                cout << "[FOR EXIT] Calculations = " << round_calculations << endl
                     << "--END FOR LOOP--" << endl;
            }
            #ifdef _WIN32
                latest_prime_commas = insert_commas(latest_prime()); // Faster update speed for console title, skip on linux
            #endif
            if (invalid == false)
            {
                task_duration = ( std::clock() - task_start ) / static_cast<double>(CLOCKS_PER_SEC);
                #ifdef _WIN32
                    previous_task_duration = task_duration;
                #endif
                if (debug >= 2) { cout << "==PRIME FOUND==";
                }
                json_config["statistics"]["Total Calculations"] = total_calculations() + round_calculations;
                json_config["statistics"]["Primes Found"] = primes_found() + 1;
                #if defined(__APPLE__) || defined(__linux__) // Don't insert commas twice for Windows
                    latest_prime_commas = insert_commas(latest_prime());
                #endif
                cout << "Found Prime [#" << insert_commas(primes_found()) << "]!  "
                     << "-->  " << latest_prime_commas << " <--  "
                     << "[Total: " << insert_commas(total_calculations()) << "]  "
                     << insert_commas(round_calculations) << " calculations in " << task_duration <<" seconds"
                     << endl;
                round_calculations = 0;

                // https://www.cplusplus.com/doc/tutorial/files/
                int successful_write = 0;
                while (successful_write < 2) {
                    config_file.open("Primer_config.json", std::ios::trunc);
                    config_file << json_config.dump(4) << endl;
                    config_file.close();
                    successful_write = 1;

                    txt_file_append.open("Primer.txt", std::ios::app);
                    txt_file_append << latest_prime() << endl;
                    txt_file_append.close();
                    //txt_file_append.close();
                    successful_write = 2;
                }

                if (debug >= 2) { std::cin.get();
                }

                new_round = true;
                break;
            }
        }

        json_config["statistics"]["Latest Prime"] = latest_prime() + 1;
        invalid = false;
        #if _WIN32
            if (previous_task_duration > 5) {
                task_duration = ( std::clock() - task_start ) / static_cast<double>(CLOCKS_PER_SEC);
                if (task_duration > 60) {
                    windows_console_title("   Elapsed: " + std::to_string(task_duration) + "s  ---  Testing: " + latest_prime_commas);
                    console_update = true;
                }
            }
            else if (console_update == true) { windows_console_title(""); }
            else { console_update = false; }
        #endif


    }

    return 0;
}
