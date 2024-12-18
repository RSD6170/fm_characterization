import sys
import pathlib
import logging
import argparse
from typing import Optional, Any

from flamapy.metamodels.fm_metamodel.models import FeatureModel
from flamapy.metamodels.fm_metamodel.transformations import UVLReader, FeatureIDEReader

from fm_characterization import FMCharacterization, PartwiseCharacterization


def read_fm_file(filename: str) -> Optional[FeatureModel]:
    try:
        if filename.endswith(".uvl"):
            return UVLReader(filename).transform()
        elif filename.endswith(".xml") or filename.endswith(".fide"):
            return FeatureIDEReader(filename).transform()
    except Exception as e:
        print(e)
        pass
    try:
        return UVLReader(filename).transform()
    except Exception as e:
        print(e)
        pass
    try:
        return FeatureIDEReader(filename).transform()
    except Exception as e:
        print(e)
        pass
    return None



def main(fm_filepath: str, mode : str) -> None:
    path = pathlib.Path(fm_filepath)
    filename = path.stem
    dir = path.parent

    # Read the feature model
    fm = read_fm_file(fm_filepath)
    if fm is None:
        raise Exception('Feature model format not supported.')
    
    characterization = PartwiseCharacterization(fm, mode)

    #print(characterization)
    #output_filepath = str(dir / f'{filename}.json')
    print("###---###")
    print(characterization.export())
    

if __name__ == '__main__':
    sys.set_int_max_str_digits(0)
    logging.basicConfig(level=logging.ERROR)
    
    parser = argparse.ArgumentParser(description='FM Characterization.')
    parser.add_argument(metavar='path', dest='path', type=str, help='Input feature model.')
    parser.add_argument("--mode", help="Subset to analyze, defaults to all", choices=["all", "metrics", "analysis_full", "analysis_light"], default="all")

    args = parser.parse_args()

    main(args.path, args.mode)
