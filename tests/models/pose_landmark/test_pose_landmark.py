# Reference: https://github.com/google-ai-edge/mediapipe-samples/blob/main/examples/pose_landmarker/python/%5BMediaPipe_Python_Tasks%5D_Pose_Landmarker.ipynb

import pytest

dependencies = ["mediapipe"]


@pytest.mark.usefixtures("manage_dependencies")
@pytest.mark.compilation_xfail
def test_pose_landmark(record_property):
    record_property("model_name", "Pose Landmark")

    import mediapipe as mp
    from mediapipe.tasks import python
    from mediapipe.tasks.python import vision

    base_options = python.BaseOptions(model_asset_path="pose_landmarker_lite.task")
    options = vision.PoseLandmarkerOptions(base_options=base_options, output_segmentation_masks=True)
    detector = vision.PoseLandmarker.create_from_options(options)

    image = mp.Image.create_from_file("test_image.jpg")

    detection_result = detector.detect(image)

    record_property("torch_ttnn", (detector.detect, image, detection_result))
