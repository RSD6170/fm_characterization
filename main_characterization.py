import sys
import pathlib
import logging
import argparse
from typing import Optional, Any

from flamapy.metamodels.fm_metamodel.models import FeatureModel
from flamapy.metamodels.fm_metamodel.transformations import UVLReader, FeatureIDEReader

from fm_characterization import FMCharacterization, PartwiseCharacterization


def read_fm_file(filenameUVL: str, filenameXML : str) -> Optional[FeatureModel]:
    try:
        return FeatureIDEReader(filenameXML).transform()
    except Exception as e:
        print(e)
        pass
    try:
        return UVLReader(filenameUVL).transform()
    except Exception as e:
        print(e)
        pass
    return None



def main(path_UVL: str, path_XML: str, mode : str) -> None:
    path = pathlib.Path(fm_filepath)
    filename = path.stem
    dir = path.parent

    # Read the feature model
    fm = read_fm_file(path_UVL, path_XML)
    if fm is None:
        raise Exception('Error in FM Parsing.')
    
    characterization = PartwiseCharacterization(fm, mode)

    #print(characterization)
    #output_filepath = str(dir / f'{filename}.json')
    print("###---###")
    print(characterization.export())
    

if __name__ == '__main__':
    sys.set_int_max_str_digits(0)
    logging.basicConfig(level=logging.ERROR)
    
    parser = argparse.ArgumentParser(description='FM Characterization.')
    parser.add_argument('pathUVL', type=str, help='Input feature model as UVL.')
    parser.add_argument('pathXML', type=str, help='Input feature model as XML.')
    parser.add_argument("--mode", help="Subset to analyze, defaults to all", choices=["all", "metrics", "analysis_full", "analysis_light"], default="all")

    args = parser.parse_args()

    main(args.pathUVL, args.pathXML, args.mode)
