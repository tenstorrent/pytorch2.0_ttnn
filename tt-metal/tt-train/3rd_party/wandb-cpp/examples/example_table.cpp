#include <cmath>

#include "wandbcpp.hpp"

int main() {
  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"table"}});
  int I = 10;
  int J = 100;

  for (int i = 0; i < I; i++) {
    wandbcpp::Table table({"x", "y"});
    for (int j = 0; j < J; j++) {
      double x = (i + 1) * std::sin(M_PI * j / J);
      double y = (i + 1) * std::cos(M_PI * j / J);
      table.add_data({x, y});
    }
    wandbcpp::log({{"mytable", table}});
  }
  wandbcpp::finish();
}
