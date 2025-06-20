#include <chrono>
#include <cmath>
#include <iostream>

#include "wandbcpp.hpp"

namespace chrono = std::chrono;
using namespace std::literals;

int main() {
  wandbcpp::init(
      {.project = "example_wandb_cpp", .tags = {"time measurement"}});

  int N = 100;

  wandbcpp::update_config({{"N", N}});

  auto begin = chrono::high_resolution_clock::now();

  for (int i = 0; i < N; i++) {
    double t = M_PI * i / N;
    double x = std::sin(M_PI * i / N);
    double y = std::cos(M_PI * i / N);
    wandbcpp::log({{"t", t}, {"x", x}, {"y", y}});
    std::cout << "i : " << i << std::endl;
  }

  auto end = chrono::high_resolution_clock::now();
  const auto elapsed_time_us_per_step =
      chrono::duration_cast<chrono::microseconds>(end - begin).count() /
      static_cast<double>(N);

  wandbcpp::update_summary(
      {{"elapsed_time_us per step", elapsed_time_us_per_step}});
  wandbcpp::finish();
}
