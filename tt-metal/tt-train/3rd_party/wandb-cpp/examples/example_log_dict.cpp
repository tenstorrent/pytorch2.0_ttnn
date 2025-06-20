#include <cmath>
#include <iostream>

#include "wandbcpp.hpp"

int main() {
  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"log_dict"}});

  int N = 100;

  for (int i = 0; i < N; i++) {
    wandbcpp::log_dict logs;
    double t = M_PI * i / N;
    double x = std::sin(M_PI * i / N);
    double y = std::cos(M_PI * i / N);
    logs.update({{"t", t}});
    logs.update({{"x", x}});
    logs.update({{"y", y}});
    wandbcpp::log(logs);
  }

  wandbcpp::save(__FILE__);
  wandbcpp::finish();
}
