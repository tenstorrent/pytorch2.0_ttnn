#include "wandbcpp.hpp"

int main() {
  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"save file"}});
  wandbcpp::save("examples/data/lena.png");  // save this source code
  wandbcpp::finish();
}
