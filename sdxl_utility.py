"""

Custom nodes for SDXL in ComfyUI

MIT License

Copyright (c) 2023 Willie Sippel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import nodes

class SDXLResolutionPresets:
    RESOLUTIONS = ["Cinematic (1536x640)", "Widescreen (1344x768)", "Photo (1216x832)", "Portrait (1152x896)", "Square (1024x1024)"]
    ASPECT = ["Horizontal", "Vertical"]

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "resolution": (SDXLResolutionPresets.RESOLUTIONS, {"default": "Square (1024x1024)"}),
                    "aspect": (SDXLResolutionPresets.ASPECT, {"default": "Horizontal"})
                    },
                }

    RETURN_TYPES = ("INT", "INT", )
    RETURN_NAMES = ("width", "height", )
    FUNCTION = "get_value"

    CATEGORY = "ws"

    def get_value(self, resolution, aspect, ):
        if resolution == "Cinematic (1536x640)":
            if aspect == "Horizontal":
                return (1536, 640)
            else:
                return (640, 1536)
        if resolution == "Widescreen (1344x768)":
            if aspect == "Horizontal":
                return (1344, 768)
            else:
                return (768, 1344)
        if resolution == "Photo (1216x832)":
            if aspect == "Horizontal":
                return (1216, 832)
            else:
                return (832, 1216)
        if resolution == "Portrait (1152x896)":
            if aspect == "Horizontal":
                return (1152, 896)
            else:
                return (896, 1152)
        if resolution == "Square (1024x1024)":
            return (1024, 1024)

NODE_CLASS_MAPPINGS = {
    "SDXLResolutionPresets": SDXLResolutionPresets,
}

# Human readable names for the nodes

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLResolutionPresets": "SDXL Resolution Presets (ws)",
}
