// Primer
// github.com/smcclennon/Primer

// Started porting Primer.py on the 5th may 2020
// Finished recoding in C++ on the 7th may 2020



#include <string>
#include <iostream>
#include <fstream>
#include <ctime>
#include <map>
#include "json.hpp"



using json = nlohmann::json;

std::string ver = "1.0.0";
std::string proj = "Primer";

int found = 0;
int calculations = 0;
bool invalid = false;
bool debug = false;
double task_duration;
std::clock_t task_start;

std::fstream config_file("Primer_config.json");
json json_config;



int latest_prime() { return json_config["statistics"]["Latest Prime"].get<int>(); }
int primes_found() { return json_config["statistics"]["Primes Found"].get<int>(); }
int total_calculations() { return json_config["statistics"]["Total Calculations"].get<int>(); }

// https://stackoverflow.com/a/24192835
std::string insert_commas(int num)
{
    std::string numWithCommas = std::to_string(num);
    int insertPosition = numWithCommas.length() - 3;
    while (insertPosition > 0)
    {
        numWithCommas.insert(insertPosition, ",");
        insertPosition -= 3;
    }
    return numWithCommas;
}

int main()
{
    using std::cout;
    using std::endl;



    try {
        if (debug) { cout << "Trying to load config" << endl;
        }
        json_config = json::parse(config_file);
    } catch (...) {
        cout << "Created Primer_config.json" << endl;
        json_config = "{\"statistics\": {\"Total Calculations\": 0, \"Primes Found\": 0, \"Latest Prime\": 0}, \"debugging\": {\"Force Unix\": \"False\"}}"_json;
    }



    if (debug) { cout << json_config.dump(4) << endl;
    }

    bool new_round = true;



    while (true)
    {
        if (new_round)
        {
            // https://stackoverflow.com/a/3220503
            task_start = std::clock();
            new_round = false;
        }


        if (debug) { cout << "\n-- RESTART WHILE TRUE --" << endl;
        }

        while (invalid == false)
        {

            if (debug) {
                cout << "[WHILE] Invalid: false" << endl
                << "[WHILE] latest_prime = " << latest_prime() << endl
                << "[WHILE] latest_prime % 2 == 0: ???" << endl
                << "[WHILE] Calculations = " << calculations << endl
                << "--START IF--" << endl;

            }


            if (latest_prime() % 2 == 0) // If even
            {
                if (debug) { cout << "latest_prime % 2 == 0: True" << endl;
                }
                //json_config["statistics"]["Total Calculations"] = total_calculations() + 1;
                calculations++;
                if (debug) { cout << "[IF] Number is even" << endl;
                }
                invalid = true;
                if (debug) { cout << "[IF] Invalid: true" << endl;
                }
                break;
                if (debug) { cout << "[IF] Failed to break" << endl;
                }
            }

            if (debug) {
                cout << "--END IF--"
                << "\nCalculations = " << calculations
                << "\nTotal calculations = " << total_calculations()
                << "\n--START FOR LOOP--" << endl;
            }


            for (int i = 3; i < latest_prime(); i+=2)
            {
                calculations++;
                if (latest_prime() % i == 0)
                {
                    calculations++;
                    if (debug) { cout << "[FOR] Number is divisible\n[FOR] Invalid: true" << endl;
                    }
                    invalid = true;
                    //break;
                    if (debug) { cout << "[FOR] Failed to break" << endl;
                    }
                }
            }
            if (debug) {
                cout << "[FOR EXIT] Calculations = " << calculations << endl
                     << "--END FOR LOOP--" << endl;
            }


            if (invalid == false)
            {
                task_duration = ( std::clock() - task_start ) / (double) CLOCKS_PER_SEC;
                if (debug) { cout << "==PRIME FOUND==";
                }
                json_config["statistics"]["Total Calculations"] = total_calculations() + calculations;
                json_config["statistics"]["Primes Found"] = primes_found() + 1;
                cout << proj << "++ v" << ver << "  "
                     << "Found Prime [#" << insert_commas(primes_found()) << "]!  "
                     << "-->  " << insert_commas(latest_prime()) << " <--  "
                     << "[Total: " << insert_commas(total_calculations()) << "]  "
                     << insert_commas(calculations) << " calculations in " << task_duration <<" seconds"
                     << endl;
                calculations = 0;

                // https://www.cplusplus.com/doc/tutorial/files/
                std::ofstream config_file("Primer_config.json");
                std::ofstream txt_file_append("Primer.txt", std::ios::out | std::ios::app);

                int successful_write = 0;
                while (successful_write < 2) {
                    if (config_file.is_open()) {
                        config_file << json_config.dump(4) << std::endl;
                        config_file.close();
                        successful_write = 1;
                    } else {
                        cout << "Unable to open file \"Primer_config.json\"" << endl; }

                    if (txt_file_append.is_open()) {
                        txt_file_append << latest_prime() << std::endl;
                        txt_file_append.close();
                        successful_write = 2;
                    } else {
                        cout << "Unable to open file \"Primer.txt\"" << endl; }
                }

                if (debug) { std::cin.get();
                }

                new_round = true;
                break;
            }
        }

        json_config["statistics"]["Latest Prime"] = latest_prime() + 1;
        invalid = false;
    }

    return 0;
}
