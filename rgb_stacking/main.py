# Copyright 2021 Deepmind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Script to run a viewer to visualize the rgb stacking environment."""

from typing import Sequence

from absl import app
from dm_control import viewer

from rgb_stacking import environment


def main(argv: Sequence[str]) -> None:

  del argv

  # Load the rgb stacking environment.
  env = environment.rgb_stacking(object_triplet='rgb_test_triplet1')

  # Launch the viewer application.
  viewer.launch(env)


if __name__ == '__main__':
  app.run(main)
