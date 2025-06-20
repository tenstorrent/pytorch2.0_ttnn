#include <cmath>
#include <iostream>
#include <thread>

#include "wandbcpp.hpp"

namespace chrono = std::chrono;
using namespace std::literals;

int main() { std::cout << (int)wandbcpp::wandb::get_mode() << std::endl; }
