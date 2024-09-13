# Reference: https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/pose_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Pose_Landmarker.ipynb

import subprocess
import sys
import pytest

dependencies = ["mediapipe"]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.compilation_xfail
def test_pose_landmark(record_property):
    record_property("model_name", "Pose Landmark")

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
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python-headless==4.8.0.74"])

    import mediapipe as mp
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision

    base_options = python.BaseOptions(model_asset_path="pose_landmarker_lite.task")
    options = vision.PoseLandmarkerOptions(base_options=base_options, output_segmentation_masks=True)
    detector = vision.PoseLandmarker.create_from_options(options)

    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "opencv-python-headless"])

    image = mp.Image.create_from_file("test_image.jpg")

    detection_result = detector.detect(image)

    record_property("torch_ttnn", (detector.detect, image, detection_result))