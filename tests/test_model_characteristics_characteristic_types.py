#
# Copyright 2019 aiohomekit team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest

from aiohomekit.model.characteristics.characteristic_types import CharacteristicsTypes


def test_getitem_forward():
    assert (
        CharacteristicsTypes[CharacteristicsTypes.ON] == "public.hap.characteristic.on"
    )


def test_getitem_reverse():
    assert (
        CharacteristicsTypes["public.hap.characteristic.on"] == CharacteristicsTypes.ON
    )


def test_getitem_unknown():
    # self.assertEqual(CharacteristicsTypes[-99], 'Unknown Characteristic -99?')
    with pytest.raises(KeyError):
        CharacteristicsTypes[99]


def test_get_uuid_forward():
    assert (
        CharacteristicsTypes.get_uuid(CharacteristicsTypes.ON)
        == "00000025-0000-1000-8000-0026BB765291"
    )


def test_get_uuid_reverse():
    assert (
        CharacteristicsTypes.get_uuid("public.hap.characteristic.on")
        == "00000025-0000-1000-8000-0026BB765291"
    )


def test_get_uuid_unknown():
    with pytest.raises(KeyError):
        CharacteristicsTypes.get_uuid("XXX")


def test_get_short():
    assert CharacteristicsTypes.get_short(CharacteristicsTypes.ON) == "on"
    assert (
        CharacteristicsTypes.get_short(
            CharacteristicsTypes.get_uuid(CharacteristicsTypes.ON)
        )
        == "on"
    )
    assert (
        CharacteristicsTypes.get_short(CharacteristicsTypes.DOOR_STATE_TARGET)
        == "door-state.target"
    )
    assert (
        CharacteristicsTypes.get_short(CharacteristicsTypes.AIR_PURIFIER_STATE_CURRENT)
        == "air-purifier.state.current"
    )
    assert CharacteristicsTypes.get_short("1a") == "lock-management.auto-secure-timeout"


def test_get_uuid_full_uuid():
    assert "0000006D-0000-1000-8000-0026BB765291" == CharacteristicsTypes.get_uuid(
        "0000006D-0000-1000-8000-0026BB765291"
    )


def test_get_uuid_short_uuid():
    assert "0000006D-0000-1000-8000-0026BB765291" == CharacteristicsTypes.get_uuid("6D")


def test_get_uuid_name():
    assert "0000006D-0000-1000-8000-0026BB765291" == CharacteristicsTypes.get_uuid(
        "public.hap.characteristic.position.current"
    )


def test_get_uuid_unknown_2():
    with pytest.raises(KeyError):
        CharacteristicsTypes.get_uuid("UNKNOWN")


def test_get_short_uuid_full_uuid():
    assert "6D" == CharacteristicsTypes.get_short_uuid(
        "0000006D-0000-1000-8000-0026BB765291"
    )


def test_get_short_uuid_name():
    assert "6D" == CharacteristicsTypes.get_short_uuid(
        "public.hap.characteristic.position.current"
    )


def test_get_short_uuid_short():
    assert "6D" == CharacteristicsTypes.get_short_uuid("6D")


def test_get_short_uuid_unknown():
    with pytest.raises(KeyError):
        CharacteristicsTypes.get_short_uuid("UNKNOWN")


def test_get_short_uuid_passthrough():
    assert (
        "0000006D-1234-1234-1234-012345678901"
        == CharacteristicsTypes.get_short_uuid("0000006D-1234-1234-1234-012345678901")
    )


def test_get_short_full_uuid():
    assert "position.current" == CharacteristicsTypes.get_short(
        "0000006D-0000-1000-8000-0026BB765291"
    )


def test_get_short_short_uuid():
    assert "position.current" == CharacteristicsTypes.get_short("6D")


def test_get_short_unknown():
    assert "Unknown Characteristic 1234" == CharacteristicsTypes.get_short("1234")


def test_getitem_short_uuid():
    assert "public.hap.characteristic.position.current" == CharacteristicsTypes["6D"]


def test_getitem_name():
    assert "6D" == CharacteristicsTypes["public.hap.characteristic.position.current"]


def test_getitem_unknown_2():
    with pytest.raises(KeyError):
        CharacteristicsTypes["UNKNOWN"]
