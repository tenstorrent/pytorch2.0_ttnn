#include "ttnn_cpp_extension/core/copy.hpp"  // для функцій копіювання
#include <ttnn/operations/copy.hpp>          // правильний заголовок замість convert.hpp
#include <torch/extension.h>

namespace ttnn_extension {

// Функція для реалізації aten::_to_copy на TTNN
at::Tensor to_copy(const at::Tensor& self, c10::optional<at::Device> device_opt, bool non_blocking, c10::optional<at::ScalarType> dtype_opt) {
    // Перевірити цільовий пристрій
    TORCH_CHECK(device_opt.has_value(), "Device must be specified for to_copy.");
    auto device = device_opt.value();

    // Якщо dtype не заданий — використовуємо dtype вихідного тензора
    auto dtype = dtype_opt.value_or(self.scalar_type());

    // Створити порожній тензор на цільовому пристрої
    auto options = self.options().dtype(dtype).device(device);
    auto out = at::empty_like(self, options, c10::nullopt);

    // Виконати копіювання
    ttnn_copy_from(out, self, non_blocking);

    return out;
}

} // namespace ttnn_extension

// Реєстрація операції в PyTorch Dispatcher
TORCH_LIBRARY_IMPL(aten, PrivateUse1, m) {
    m.def("div.Tensor", tt_eager::ops::binary::ttnn_div_tensor);

}
