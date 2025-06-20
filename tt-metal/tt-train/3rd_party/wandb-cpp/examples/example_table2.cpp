#include "wandbcpp.hpp"

int main() {
  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"table"}});
  int I = 10;
  for (int i = 0; i < I; i++) {
    wandbcpp::Table table({"x", "y"}, {{"poyo", i}, {"hoge", i + 1}});
    wandbcpp::log({{"table", table}});
  }
  wandbcpp::finish();
}
