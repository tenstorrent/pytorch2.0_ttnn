#include <array>
#include <random>

#include "src/utils.hpp"
#include "wandbcpp.hpp"

std::array<double, 3> gen_random_point() {
  static std::random_device seed_gen;
  static std::mt19937 engine(seed_gen());
  static std::uniform_real_distribution<> dist(-1.0, 1.0);
  return {dist(engine), dist(engine), dist(engine)};
}

int main(int argc, char const* argv[]) {
  namespace np = wandbcpp::numpy;

  wandbcpp::init(
      {.project = "example_wandb_cpp", .tags = {"object3d", "lidar"}});

  int num_points = 300;

  std::vector<std::array<double, 3>> point_cloud(num_points);

  std::generate(point_cloud.begin(), point_cloud.end(), &gen_random_point);

  auto point_cloud_lst =
      wandbcpp::topylist(point_cloud.begin(), point_cloud.end());

  std::vector<std::array<double, 3>> box_corners = {
      {0, 0, 0}, {0, 1, 0}, {0, 0, 1}, {1, 0, 0},
      {1, 1, 0}, {0, 1, 1}, {1, 0, 1}, {1, 1, 1},
  };

  auto box_corners_lst =
      wandbcpp::topylist(box_corners.begin(), box_corners.end());

  auto box = np::ndarray(wandbcpp::py_list(
      wandbcpp::py_dict({{"corners", box_corners_lst},
                         {"color", wandbcpp::py_list(123, 321, 111)}})));

  wandbcpp::Object3D obj{
      wandbcpp::py_dict({{"type", "lidar/beta"},                    //
                         {"points", np::ndarray{point_cloud_lst}},  //
                         {"boxes", box}})};

  wandbcpp::log({{"obj3d", obj}});

  wandbcpp::finish();

  return 0;
}
