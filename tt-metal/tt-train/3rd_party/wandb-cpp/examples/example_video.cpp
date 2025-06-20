#ifdef USE_OPENCV
#include <opencv2/opencv.hpp>
#endif
#include "wandbcpp.hpp"

int main() {
#ifdef USE_OPENCV

  cv::VideoCapture cap("examples/data/parrot.mp4");

  if (!cap.isOpened()) {
    std::cerr << "Error: Video file not opened." << std::endl;
    return 1;
  }

  std::vector<cv::Mat> frames;

  while (true) {
    cv::Mat frame;
    cap >> frame;
    if (frame.empty()) break;

    frames.push_back(frame);
  }
  std::cout << "Number of frames: " << frames.size() << std::endl;

  wandbcpp::init({.project = "example_wandb_cpp", .tags = {"video"}});

  wandbcpp::log({{"video", wandbcpp::Video(frames.begin(), frames.end())}});

  wandbcpp::finish();

#endif
}
