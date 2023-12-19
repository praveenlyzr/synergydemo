# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
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

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="VoiceBot",
        page_icon="👋",
    )
    from PIL import Image

    image = Image.open("lyzr-logo.png")
    st.image(image, caption="", width=150)

    st.write("# Welcome to VoiceBot! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        VoiceBot is a powerful audio processing SDK built by Lyzr AI.
        **👈 Select a demo from the sidebar** to see some examples
        of what VoiceBot can do!
        ### Want to learn more?
        - Check out [lyzr.ai](https://www.lyzr.ai/)
        - Jump into our [documentation](https://docs.lyzr.ai/homepage)
        - Ask a question in our [community
          forums](https://discord.com/invite/P6HCMQ9TRX)
        
    """
    )


if __name__ == "__main__":
    run()
