#!/bin/bash

# Exit immediately if any command fails
set -e

echo "🔧 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Setting PyTorch CPU wheel index..."
python3 -m pip config set global.extra-index-url https://download.pytorch.org/whl/cpu

echo "📥 Installing dev requirements..."
pip install -r requirements-dev.txt

echo "♻️  Reinstalling specific pip version..."
pip install --force-reinstall pip==21.2.4

echo "📥 Installing build tools..."
python3 -m pip install numpy setuptools wheel

echo "🔗 Installing project in editable mode..."
python3 -m pip install -e .

echo "📁 Entering cpp_extension directory..."
pushd torch_ttnn/cpp_extension

echo "🔄 Syncing git submodules..."
git submodule sync
git submodule update --init --recursive
git submodule foreach 'git lfs fetch --all && git lfs pull'

echo "📦 Installing tt-metal dependencies..."
./third-party/tt-metal/install_dependencies.sh

echo "🛠️ Building C++ extension..."
./build_cpp_extension.sh Release

# echo "🌐 Exporting TT_METAL_HOME..."
# export TT_METAL_HOME="$(pwd)/third-party/tt-metal"
# echo "TT_METAL_HOME set to $TT_METAL_HOME"

# popd

# echo "✅ Setup complete!"
