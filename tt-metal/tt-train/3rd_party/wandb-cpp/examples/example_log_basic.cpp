#include <cmath>
#include <iostream>

#include "wandbcpp.hpp"

int main() {
  wandbcpp::init(
      {.project = "example_wandb_cpp", .tags = {"basic"}, .group = "abc"});

  int N = 100;

  wandbcpp::update_config({{"N", N}, {"mode", "abc"}});

  for (int i = 0; i < N; i++) {
    double t = M_PI * i / N;
    double x = std::sin(M_PI * i / N);
    double y = std::cos(M_PI * i / N);
    wandbcpp::log({{"t", t}, {"x", x}, {"y", y}});
    std::cout << "i : " << i << std::endl;
  }

  wandbcpp::update_summary({{"success", true}});

  wandbcpp::finish();
}
