# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-36m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


# Variables with simple values

ANTIALIAS_BEST = 6
ANTIALIAS_DEFAULT = 0
ANTIALIAS_FAST = 4
ANTIALIAS_GOOD = 5
ANTIALIAS_GRAY = 2
ANTIALIAS_NONE = 1
ANTIALIAS_SUBPIXEL = 3

CONTENT_ALPHA = 8192
CONTENT_COLOR = 4096

CONTENT_COLOR_ALPHA = 12288

EXTEND_NONE = 0
EXTEND_PAD = 3
EXTEND_REFLECT = 2
EXTEND_REPEAT = 1

FILL_RULE_EVEN_ODD = 1

FILL_RULE_WINDING = 0

FILTER_BEST = 2
FILTER_BILINEAR = 4
FILTER_FAST = 0
FILTER_GAUSSIAN = 5
FILTER_GOOD = 1
FILTER_NEAREST = 3

FONT_SLANT_ITALIC = 1
FONT_SLANT_NORMAL = 0
FONT_SLANT_OBLIQUE = 2

FONT_WEIGHT_BOLD = 1
FONT_WEIGHT_NORMAL = 0

FORMAT_A1 = 3
FORMAT_A8 = 2
FORMAT_ARGB32 = 0
FORMAT_INVALID = -1

FORMAT_RGB16_565 = 4

FORMAT_RGB24 = 1
FORMAT_RGB30 = 5

HAS_ATSUI_FONT = 0

HAS_FT_FONT = 1

HAS_GLITZ_SURFACE = 0

HAS_IMAGE_SURFACE = 1

HAS_MIME_SURFACE = 1

HAS_PDF_SURFACE = 1

HAS_PNG_FUNCTIONS = 1

HAS_PS_SURFACE = 1

HAS_QUARTZ_SURFACE = 0

HAS_RECORDING_SURFACE = 1

HAS_SCRIPT_SURFACE = 1

HAS_SVG_SURFACE = 1

HAS_TEE_SURFACE = 1

HAS_USER_FONT = 1

HAS_WIN32_FONT = 0
HAS_WIN32_SURFACE = 0

HAS_XCB_SURFACE = 1

HAS_XLIB_SURFACE = 1

HINT_METRICS_DEFAULT = 0
HINT_METRICS_OFF = 1
HINT_METRICS_ON = 2

HINT_STYLE_DEFAULT = 0
HINT_STYLE_FULL = 4
HINT_STYLE_MEDIUM = 3
HINT_STYLE_NONE = 1
HINT_STYLE_SLIGHT = 2

LINE_CAP_BUTT = 0
LINE_CAP_ROUND = 1
LINE_CAP_SQUARE = 2

LINE_JOIN_BEVEL = 2
LINE_JOIN_MITER = 0
LINE_JOIN_ROUND = 1

MIME_TYPE_JP2 = 'image/jp2'
MIME_TYPE_JPEG = 'image/jpeg'
MIME_TYPE_PNG = 'image/png'

MIME_TYPE_UNIQUE_ID = 'application/x-cairo.uuid'

MIME_TYPE_URI = 'text/x-uri'

OPERATOR_ADD = 12
OPERATOR_ATOP = 5
OPERATOR_CLEAR = 0

OPERATOR_COLOR_BURN = 20
OPERATOR_COLOR_DODGE = 19

OPERATOR_DARKEN = 17
OPERATOR_DEST = 6

OPERATOR_DEST_ATOP = 10
OPERATOR_DEST_IN = 8
OPERATOR_DEST_OUT = 9
OPERATOR_DEST_OVER = 7

OPERATOR_DIFFERENCE = 23
OPERATOR_EXCLUSION = 24

OPERATOR_HARD_LIGHT = 21

OPERATOR_HSL_COLOR = 27
OPERATOR_HSL_HUE = 25
OPERATOR_HSL_LUMINOSITY = 28
OPERATOR_HSL_SATURATION = 26

OPERATOR_IN = 3
OPERATOR_LIGHTEN = 18
OPERATOR_MULTIPLY = 14
OPERATOR_OUT = 4
OPERATOR_OVER = 2
OPERATOR_OVERLAY = 16
OPERATOR_SATURATE = 13
OPERATOR_SCREEN = 15

OPERATOR_SOFT_LIGHT = 22

OPERATOR_SOURCE = 1
OPERATOR_XOR = 11

PATH_CLOSE_PATH = 3

PATH_CURVE_TO = 2

PATH_LINE_TO = 1

PATH_MOVE_TO = 0

PDF_VERSION_1_4 = 0
PDF_VERSION_1_5 = 1

PS_LEVEL_2 = 0
PS_LEVEL_3 = 1

REGION_OVERLAP_IN = 0
REGION_OVERLAP_OUT = 1
REGION_OVERLAP_PART = 2

SCRIPT_MODE_ASCII = 0
SCRIPT_MODE_BINARY = 1

STATUS_CLIP_NOT_REPRESENTABLE = 22

STATUS_DEVICE_ERROR = 35
STATUS_DEVICE_FINISHED = 37

STATUS_DEVICE_TYPE_MISMATCH = 34

STATUS_FILE_NOT_FOUND = 18

STATUS_FONT_TYPE_MISMATCH = 25

STATUS_INVALID_CLUSTERS = 29
STATUS_INVALID_CONTENT = 15
STATUS_INVALID_DASH = 19

STATUS_INVALID_DSC_COMMENT = 20

STATUS_INVALID_FORMAT = 16
STATUS_INVALID_INDEX = 21
STATUS_INVALID_MATRIX = 5

STATUS_INVALID_MESH_CONSTRUCTION = 36

STATUS_INVALID_PATH_DATA = 9

STATUS_INVALID_POP_GROUP = 3

STATUS_INVALID_RESTORE = 2
STATUS_INVALID_SIZE = 32
STATUS_INVALID_SLANT = 30
STATUS_INVALID_STATUS = 6
STATUS_INVALID_STRIDE = 24
STATUS_INVALID_STRING = 8
STATUS_INVALID_VISUAL = 17
STATUS_INVALID_WEIGHT = 31

STATUS_JBIG2_GLOBAL_MISSING = 38

STATUS_LAST_STATUS = 43

STATUS_NEGATIVE_COUNT = 28

STATUS_NO_CURRENT_POINT = 4

STATUS_NO_MEMORY = 1

STATUS_NULL_POINTER = 7

STATUS_PATTERN_TYPE_MISMATCH = 14

STATUS_READ_ERROR = 10

STATUS_SUCCESS = 0

STATUS_SURFACE_FINISHED = 12

STATUS_SURFACE_TYPE_MISMATCH = 13

STATUS_TEMP_FILE_ERROR = 23

STATUS_USER_FONT_ERROR = 27
STATUS_USER_FONT_IMMUTABLE = 26

STATUS_USER_FONT_NOT_IMPLEMENTED = 33

STATUS_WRITE_ERROR = 11

SUBPIXEL_ORDER_BGR = 2
SUBPIXEL_ORDER_DEFAULT = 0
SUBPIXEL_ORDER_RGB = 1
SUBPIXEL_ORDER_VBGR = 4
SUBPIXEL_ORDER_VRGB = 3

SURFACE_OBSERVER_NORMAL = 0

SURFACE_OBSERVER_RECORD_OPERATIONS = 1

SVG_VERSION_1_1 = 0
SVG_VERSION_1_2 = 1

TEXT_CLUSTER_FLAG_BACKWARD = 1

version = '1.16.2'

# functions

def cairo_version(*args, **kwargs): # real signature unknown
    pass

def cairo_version_string(*args, **kwargs): # real signature unknown
    pass

# classes

from .Antialias import Antialias
from .Error import Error
from .CairoError import CairoError
from .Content import Content
from .Context import Context
from .Device import Device
from .Extend import Extend
from .FillRule import FillRule
from .Filter import Filter
from .FontFace import FontFace
from .FontOptions import FontOptions
from .FontSlant import FontSlant
from .FontWeight import FontWeight
from .Format import Format
from .Glyph import Glyph
from .Pattern import Pattern
from .Gradient import Gradient
from .HintMetrics import HintMetrics
from .HintStyle import HintStyle
from .Surface import Surface
from .ImageSurface import ImageSurface
from .LinearGradient import LinearGradient
from .LineCap import LineCap
from .LineJoin import LineJoin
from .Matrix import Matrix
from .MeshPattern import MeshPattern
from .Operator import Operator
from .Path import Path
from .PathDataType import PathDataType
from .PDFSurface import PDFSurface
from .PDFVersion import PDFVersion
from .PSLevel import PSLevel
from .PSSurface import PSSurface
from .RadialGradient import RadialGradient
from .RasterSourcePattern import RasterSourcePattern
from .RecordingSurface import RecordingSurface
from .Rectangle import Rectangle
from .RectangleInt import RectangleInt
from .Region import Region
from .RegionOverlap import RegionOverlap
from .ScaledFont import ScaledFont
from .ScriptDevice import ScriptDevice
from .ScriptMode import ScriptMode
from .ScriptSurface import ScriptSurface
from .SolidPattern import SolidPattern
from .Status import Status
from .SubpixelOrder import SubpixelOrder
from .SurfaceObserverMode import SurfaceObserverMode
from .SurfacePattern import SurfacePattern
from .SVGSurface import SVGSurface
from .SVGVersion import SVGVersion
from .TeeSurface import TeeSurface
from .TextCluster import TextCluster
from .TextClusterFlags import TextClusterFlags
from .TextExtents import TextExtents
from .ToyFontFace import ToyFontFace
from .XCBSurface import XCBSurface
from .XlibSurface import XlibSurface
# variables with complex values

CAPI = None # (!) real value is '<capsule object "cairo.CAPI" at 0x7fc704649c30>'

version_info = (
    1,
    16,
    2,
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc704699828>'

__spec__ = None # (!) real value is "ModuleSpec(name='cairo._cairo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc704699828>, origin='/usr/lib/python3/dist-packages/cairo/_cairo.cpython-36m-x86_64-linux-gnu.so')"

