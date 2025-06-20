#include "src/wandb_object.hpp"

int main(int argc, char const *argv[]) {
  using namespace wandbcpp::internal::object;
  Py_Initialize();
  PyBasicType i(1);
  std::cout << i << std::endl;
  Py_Finalize();
  return 0;
}
