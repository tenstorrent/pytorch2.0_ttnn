#ifdef USE_OPENCV
#include <opencv2/opencv.hpp>
#endif
#include "wandbcpp.hpp"

int main()
{
#ifdef USE_OPENCV
  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"image"}});
  cv::Mat img = cv::imread("examples/data/lena.png");
  wandbcpp::log({{"image_from_array", wandbcpp::Image(img)}});
  wandbcpp::log(
      {{"image_from_path", wandbcpp::Image("examples/data/lena.png")}});
  wandbcpp::finish();
#endif
}
