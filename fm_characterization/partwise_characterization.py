import json
from typing import Any, Optional

from flamapy.metamodels.fm_metamodel.models import FeatureModel

from fm_characterization import FMProperty, FMAnalysis, FMMetadata, FMMetrics, FMPropertyMeasure

SPACE = ' '


class PartwiseCharacterization:

    def __init__(self, model: FeatureModel, mode: str)-> None:
        self.parting_symbol = " "
        self.mode = mode
        self.metadata = FMMetadata(model)
        match mode:
            case 'all':
                self.metrics = FMMetrics(model)
                self.analysis = FMAnalysis(model, False)
            case 'metrics':
                self.metrics = FMMetrics(model)
            case 'analysis_full':
                self.analysis = FMAnalysis(model, False)
            case 'analysis_light':
                self.analysis = FMAnalysis(model, True)
            case _:
                raise ValueError('Unknown mode')


    def __str__(self) -> str:
        lines = [f'Mode = {self.mode}', 'METADATA']
        for property in self.metadata.get_metadata():
            name = property.property.name
            value = str(property.value)
            lines.append(f'{name}: {value}')

        lines.append('METRICS')
        for property in self.metrics.get_metrics():
            indentation = SPACE * get_parents_numbers(property.property)
            name = property.property.name
            value = str(property.value) if property.size is None else str(property.size)
            ratio = f' ({str(property.ratio * 100)}%)' if property.ratio is not None else ''
            lines.append(f'{indentation}{name}: {value}{ratio}')

        lines.append('ANALYSIS')
        for property in self.analysis.get_analysis():
            indentation = SPACE * get_parents_numbers(property.property)
            name = property.property.name
            value = str(property.value) if property.size is None else str(property.size)
            ratio = f' ({str(property.ratio * 100)}%)' if property.ratio is not None else ''
            lines.append(f'{indentation}{name}: {value}{ratio}')
        return '\n'.join(lines)

    def writeApprox(self, isApprox : bool) -> str:
            return "ANALYSIS/isApprox/value" + self.parting_symbol + str(isApprox)

    def export(self) -> str:
        lines = []
        match self.mode:
            case 'all':
                lines.extend((self.create_export_array(self.metrics.get_metrics(), "METRICS")))
                lines.extend((self.create_export_array(self.analysis.get_analysis(), "ANALYSIS")))
                lines.append((self.writeApprox(self.analysis.isApproximation())))
            case 'metrics':
                lines.extend((self.create_export_array(self.metrics.get_metrics(), "METRICS")))
            case 'analysis_full':
                lines.extend((self.create_export_array(self.analysis.get_analysis(), "ANALYSIS")))
                lines.append((self.writeApprox(self.analysis.isApproximation())))
            case 'analysis_light':
                lines.extend((self.create_export_array(self.analysis.get_analysis(), "ANALYSIS")))
                lines.append((self.writeApprox(self.analysis.isApproximation())))
            case _:
                raise ValueError('Unknown mode')
        return '\n'.join(lines)



    def create_export_array(self, measures: [FMPropertyMeasure], prefix: str) -> [str]:
        lines = []
        for property in measures:
            parents = get_parents(property.property)
            name = f"{prefix}"
            for parent in parents:
                name = f'{name}/{parent.name}'
            name = f'{name}/{property.property.name}'
            name = name.replace(" ", "_")

            value = str(property.value) if property.size is None else str(property.size)
            lines.append(f'{name + "/value"}{self.parting_symbol}{value}')
            if property.ratio is not None:
                ratio = property.ratio if property.ratio is not None else ''
                lines.append(f'{name + "/ratio"}{self.parting_symbol}{ratio}')
        return lines


def get_parents(property: FMProperty) -> list[FMProperty]:
    if property.parent is None:
        return []
    else:
        return get_parents(property.parent) + [property.parent]


def get_parents_numbers(property: FMProperty) -> int:
    if property.parent is None:
        return 1
    return 1 + get_parents_numbers(property.parent)