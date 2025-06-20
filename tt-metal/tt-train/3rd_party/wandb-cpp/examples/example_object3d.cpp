#include <array>
#include <random>

#include "wandbcpp.hpp"

std::array<double, 3> gen_random_point() {
  static std::random_device seed_gen;
  static std::mt19937 engine(seed_gen());
  static std::uniform_real_distribution<> dist(-1.0, 1.0);
  return {dist(engine), dist(engine), dist(engine)};
}

int main(int argc, char const* argv[]) {
  namespace np = wandbcpp::numpy;

  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"object3d"}});

  int num_points = 300;

  std::vector<std::array<double, 3>> point_cloud(num_points);

  std::generate(point_cloud.begin(), point_cloud.end(), &gen_random_point);

  auto lst = wandbcpp::topylist(point_cloud.begin(), point_cloud.end());

  wandbcpp::log({{"obj3d", wandbcpp::Object3D{np::ndarray{lst}}}});

  wandbcpp::finish();

  return 0;
}
