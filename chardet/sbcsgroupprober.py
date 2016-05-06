######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Universal charset detector code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 2001
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
#   Shy Shalom - original C code
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################

from .charsetgroupprober import CharSetGroupProber
from .sbcharsetprober import SingleByteCharSetProber
from .langcyrillicmodel import (Win1251CyrillicModel, KOI8rModel,
                                Latin5CyrillicModel, MacCyrillicModel,
                                IBM866Model, IBM855Model)
from .langbulgarianmodel import Latin5BulgarianModel, Win1251BulgarianModel
from .langgermanmodel import ISO_8859_1_German_Model, Windows_1252_German_Model
from .langczechmodel import ISO_8859_2_Czech_Model, Windows_1250_Czech_Model
from .langcroatianmodel import ISO_8859_2_Croatian_Model, Windows_1250_Croatian_Model
from .langgreekmodel import ISO_8859_7_Greek_Model, Windows_1253_Greek_Model
from .langhungarianmodel import ISO_8859_2_Hungarian_Model, Windows_1250_Hungarian_Model
from .langpolishmodel import ISO_8859_2_Polish_Model, Windows_1250_Polish_Model
from .langromanianmodel import ISO_8859_2_Romanian_Model, Windows_1250_Romanian_Model
from .langslovakmodel import ISO_8859_2_Slovak_Model, Windows_1250_Slovak_Model
from .langslovenemodel import ISO_8859_2_Slovene_Model, Windows_1250_Slovene_Model
from .langturkishmodel import ISO_8859_9_Turkish_Model, Windows_1254_Turkish_Model
from .langhebrewmodel import Win1255HebrewModel
from .langthaimodel import TIS620ThaiModel
from .hebrewprober import HebrewProber


class SBCSGroupProber(CharSetGroupProber):
    def __init__(self):
        super(SBCSGroupProber, self).__init__()
        self.probers = [
            SingleByteCharSetProber(Win1251CyrillicModel),
            SingleByteCharSetProber(KOI8rModel),
            SingleByteCharSetProber(Latin5CyrillicModel),
            SingleByteCharSetProber(MacCyrillicModel),
            SingleByteCharSetProber(IBM866Model),
            SingleByteCharSetProber(IBM855Model),
            SingleByteCharSetProber(Latin5BulgarianModel),
            SingleByteCharSetProber(Win1251BulgarianModel),
            SingleByteCharSetProber(ISO_8859_2_Czech_Model),
            SingleByteCharSetProber(Windows_1250_Czech_Model),
            SingleByteCharSetProber(ISO_8859_2_Croatian_Model),
            SingleByteCharSetProber(Windows_1250_Croatian_Model),
            SingleByteCharSetProber(ISO_8859_2_Hungarian_Model),
            SingleByteCharSetProber(Windows_1250_Hungarian_Model),
            SingleByteCharSetProber(ISO_8859_2_Polish_Model),
            SingleByteCharSetProber(Windows_1250_Polish_Model),
            SingleByteCharSetProber(ISO_8859_2_Romanian_Model),
            SingleByteCharSetProber(Windows_1250_Romanian_Model),
            SingleByteCharSetProber(ISO_8859_2_Slovak_Model),
            SingleByteCharSetProber(Windows_1250_Slovak_Model),
            SingleByteCharSetProber(ISO_8859_2_Slovene_Model),
            SingleByteCharSetProber(Windows_1250_Slovene_Model),
            SingleByteCharSetProber(ISO_8859_7_Greek_Model),
            SingleByteCharSetProber(Windows_1253_Greek_Model),
            SingleByteCharSetProber(ISO_8859_1_German_Model),
            SingleByteCharSetProber(Windows_1252_German_Model),
            SingleByteCharSetProber(ISO_8859_9_Turkish_Model),
            SingleByteCharSetProber(Windows_1254_Turkish_Model),
            SingleByteCharSetProber(TIS620ThaiModel),
        ]
        hebrew_prober = HebrewProber()
        logical_hebrew_prober = SingleByteCharSetProber(Win1255HebrewModel, False, hebrew_prober)
        visual_hebrew_prober = SingleByteCharSetProber(Win1255HebrewModel, True, hebrew_prober)
        hebrew_prober.set_model_probers(logical_hebrew_prober, visual_hebrew_prober)
        self.probers.extend([hebrew_prober, logical_hebrew_prober, visual_hebrew_prober])

        self.reset()
