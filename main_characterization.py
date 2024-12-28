import sys
import pathlib
import logging
import argparse
import resource
import os
from typing import Optional, Any

from flamapy.metamodels.fm_metamodel.models import FeatureModel
from flamapy.metamodels.fm_metamodel.transformations import UVLReader, FeatureIDEReader

from fm_characterization import FMCharacterization, PartwiseCharacterization


def read_fm_file(filenameUVL: str, filenameXML : str) -> Optional[FeatureModel]:
    try:
        return FeatureIDEReader(filenameXML).transform()
    except Exception as e:
        print(e)
        print("Failed FeatureIDE XML parsing!")
    except:
        print("Failed FeatureIDE XML parsing with Error!")
    try:
        return UVLReader(filenameUVL).transform()
    except Exception as e:
        print(e)
        print("Failed UVL parsing!")
    except:
        print("Failed FeatureIDE XML parsing with Error!")
    return None



def main(path_UVL: str, path_XML: str, mode : str) -> None:

    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    print(f"Old mem limits: {soft / 1024 / 1024} MB soft, {hard / 1024 / 1024} MB hard")
    if 'SLURM_MEM_PER_NODE' in os.environ:
        maxMem = int( int(os.environ.get('SLURM_MEM_PER_NODE')) * 1024 * 1024 * 0.70 )
        print(f"New mem limits: {maxMem / 1024 / 1024} MB soft, {hard / 1024 / 1024} MB hard")
        resource.setrlimit(resource.RLIMIT_AS, (maxMem, hard))

    # Read the feature model
    fm = read_fm_file(path_UVL, path_XML)
    if fm is None:
        print("Error in FM Parsing.")
        raise Exception('Error in FM Parsing.')
    
    characterization = PartwiseCharacterization(fm, mode)
    print("Computation successful!")

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
