"""Auto-generated data validation schema. DO NOT EDIT MANUALLY."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class GeneratedSchema:
    field_1: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 1'})
    field_2: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 2'})
    field_3: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 3'})
    field_4: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 4'})
    field_5: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 5'})
    field_6: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 6'})
    field_7: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 7'})
    field_8: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 8'})
    field_9: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 9'})
    field_10: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 10'})
    field_11: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 11'})
    field_12: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 12'})
    field_13: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 13'})
    field_14: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 14'})
    field_15: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 15'})
    field_16: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 16'})
    field_17: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 17'})
    field_18: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 18'})
    field_19: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 19'})
    field_20: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 20'})
    field_21: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 21'})
    field_22: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 22'})
    field_23: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 23'})
    field_24: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 24'})
    field_25: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 25'})
    field_26: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 26'})
    field_27: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 27'})
    field_28: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 28'})
    field_29: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 29'})
    field_30: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 30'})
    field_31: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 31'})
    field_32: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 32'})
    field_33: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 33'})
    field_34: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 34'})
    field_35: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 35'})
    field_36: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 36'})
    field_37: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 37'})
    field_38: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 38'})
    field_39: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 39'})
    field_40: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 40'})
    field_41: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 41'})
    field_42: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 42'})
    field_43: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 43'})
    field_44: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 44'})
    field_45: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 45'})
    field_46: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 46'})
    field_47: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 47'})
    field_48: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 48'})
    field_49: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 49'})
    field_50: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 50'})
    field_51: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 51'})
    field_52: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 52'})
    field_53: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 53'})
    field_54: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 54'})
    field_55: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 55'})
    field_56: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 56'})
    field_57: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 57'})
    field_58: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 58'})
    field_59: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 59'})
    field_60: Optional[str] = field(default=None, metadata={'description': 'Auto-generated field 60'})

    def validate(self) -> bool:
        return True


def from_dict(data: dict) -> GeneratedSchema:
    valid_keys = {f for f in GeneratedSchema.__dataclass_fields__}
    return GeneratedSchema(**{k: v for k, v in data.items() if k in valid_keys})
