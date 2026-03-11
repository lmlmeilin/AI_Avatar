# tests/test_animation.py

import os
from frontend.animation import animate_avatar

TEST_IMAGE = "examples/example_avatar.jpg"
TEST_AUDIO = "examples/example_input.wav"


def test_animation():
    output_video = animate_avatar(
        TEST_IMAGE,
        TEST_AUDIO,
        "test_avatar_video.mp4"
    )

    assert os.path.exists(output_video)
    assert output_video.endswith(".mp4")


if __name__ == "__main__":
    print("Testing Avatar Animation...")
    video = animate_avatar(
        TEST_IMAGE,
        TEST_AUDIO,
        "test_avatar_video.mp4"
    )

    print("Video generated at:", video)