#include "wandbcpp.hpp"

int main() {
  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"table"}});
  wandbcpp::Table table;
  std::vector<double> x = {1.0, 2.0, 3.0};
  std::vector<int> y = {4, 5, 6};
  table.add_column("x", {x.begin(), x.end()});
  table.add_column("y", {y.begin(), y.end()});
  wandbcpp::log({{"table", table}});
  wandbcpp::finish();
}
