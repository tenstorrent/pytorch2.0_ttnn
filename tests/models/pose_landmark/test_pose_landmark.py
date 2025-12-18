# Reference: https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/pose_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Pose_Landmarker.ipynb

import subprocess
import sys
from pathlib import Path
import os
import pytest

dependencies = ["mediapipe"]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.compilation_xfail
def test_pose_landmark(record_property):
    record_property("model_name", "Pose Landmark")

    """
    Forcely do `git lfs pull` to make sure the LFS files needed by this test are available.
    """
    subprocess.run(["git", "lfs", "pull"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    """
    Workaround!
    -----------
    We decided to install the Python package below within the test, rather than
    using the typical approach with the `dependencies` variable mentioned above.
    The reason is that we want to overwrite the dependencies installed by the
    standard method and ensure we are using the exact package specified below.
    If we don't, we may unintentionally use a package that requires GPU support.

    Here's the background: this test uses the Pose Landmark model from the `mediapipe`
    package, which we need to install. However, installing this package also
    pulls in a dependent package, `opencv-python`, which unfortunately requires
    GPU support. Fortunately, we found a lightweight alternative,
    `opencv-python-headless`, that does not require GPU support. Since we can't
    prevent the installation of the undesired package, we install the preferred
    one afterward to ensure it is being used. This is the most efficient
    workaround I can think of.
    """
    # Uninstall the GPU version of opencv packages.
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "opencv-python", "opencv-contrib-python"])
    # Install the CPU version of opencv package.
    # Need `--force-reinstall` to handle the case that this CPU opencv has been
    # installed before this test, which leads to the ignorance of the following
    # installation if without `--force-reinstall`.
    # However, this package actually becomes broken and needs reinstallation
    # because some of the common dependencies between GPU and CPU opencv were
    # uninstalled by the above uninstallation of GPU opencv.
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--force-reinstall", "opencv-python-headless==4.8.0.74"]
    )

    import mediapipe as mp
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision

    model_asset_path = Path(__file__).parent / "pose_landmarker_lite.task"
    file_size = os.path.getsize(str(model_asset_path))
    print(f"File size of pose_landmarker_lite.task is {file_size} bytes.")

    base_options = python.BaseOptions(model_asset_path=str(model_asset_path))
    options = vision.PoseLandmarkerOptions(base_options=base_options, output_segmentation_masks=True)
    detector = vision.PoseLandmarker.create_from_options(options)

    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "opencv-python-headless"])

    image_path = Path(__file__).parent / "test_image.jpg"
    image = mp.Image.create_from_file(str(image_path))

    detection_result = detector.detect(image)

    record_property("torch_ttnn", (detector.detect, image, detection_result))
