#!/usr/bin/env python3
"""
Koyeb Test Script for Stable Diffusion 3.5 Medium
Tests the implementation from the main repository
"""

import sys
import os
import time
from datetime import datetime

def main():
    print("🎯 Testing Stable Diffusion 3.5 Medium from Main Repository")
    print("Branch: add-stable-diffusion-3-5-medium-clean")
    print("=" * 60)
    
    # Add the current directory to Python path
    sys.path.insert(0, os.getcwd())
    
    # Check Python version
    print(f"🐍 Python: {sys.version}")
    
    try:
        import torch
        print(f"✅ PyTorch: {torch.__version__}")
        print(f"🔥 CUDA available: {torch.cuda.is_available()}")
        
        if torch.cuda.is_available():
            print(f"🔥 CUDA version: {torch.version.cuda}")
            print(f"🔥 GPU count: {torch.cuda.device_count()}")
            for i in range(torch.cuda.device_count()):
                print(f"🔥 GPU {i}: {torch.cuda.get_device_name(i)}")
        
    except ImportError as e:
        print(f"❌ PyTorch import failed: {e}")
        return 1
    
    try:
        import diffusers
        print(f"✅ Diffusers: {diffusers.__version__}")
    except ImportError as e:
        print(f"❌ Diffusers import failed: {e}")
        return 1
    
    try:
        import psutil
        print(f"✅ psutil available")
    except ImportError as e:
        print(f"❌ psutil import failed: {e}")
        return 1
    
    # Test importing our test modules
    print("\n🧪 Testing SD 3.5 Medium implementation...")
    
    try:
        # Import the test class
        from tests.models.stable_diffusion.test_stable_diffusion_3_5_medium import ThisTester
        print("✅ Successfully imported ThisTester from test_stable_diffusion_3_5_medium.py")
        
        # Test model loading
        print("📦 Testing model loading...")
        tester = ThisTester("Stable Diffusion 3.5 Medium", "eval")
        print("✅ Model loaded successfully")
        
        # Test inference
        print("🎬 Testing inference...")
        start_time = time.time()
        results = tester.test_model()
        inference_time = time.time() - start_time
        fps = 1.0 / inference_time if inference_time > 0 else 0
        
        print(f"✅ Inference completed in {inference_time:.2f} seconds")
        print(f"📊 FPS: {fps:.3f}")
        
        # Performance validation
        if fps >= 0.3:
            print("✅ TARGET ACHIEVED! Performance meets or exceeds 0.3 FPS")
        else:
            print(f"⚠️ TARGET NOT MET: {fps:.3f} FPS < 0.3 FPS target")
        
        # Results summary
        print("\n" + "=" * 60)
        print("📊 TEST RESULTS")
        print("=" * 60)
        print(f"🎯 Target FPS: 0.3")
        print(f"📈 Achieved FPS: {fps:.3f}")
        print(f"📉 Inference time: {inference_time:.2f} seconds")
        print(f"🖥️ Device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
        print(f"⏰ Test completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        print("\n🏁 Test completed successfully!")
        return 0
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
