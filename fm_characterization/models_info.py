NAME = 0
DESCRIPTION = 1
AUTHOR = 2
YEAR = 3
REFERENCE = 4
KEYWORDS = 5
DOMAIN = 6
FILENAME = 7

MODELS = [
    {NAME: 'Pizzas',
     DESCRIPTION: 'Basic feature model representing a product line for pizzas.',
     AUTHOR: 'Alexander Knüppel et al.',
     YEAR: 2017,
     REFERENCE: 'https://doi.org/10.1145/3106237.3106252',
     KEYWORDS: ['food', 'pizza', 'restaurant'],
     DOMAIN: 'restauration',
     FILENAME: 'Pizzas.uvl',
    },
    {NAME: 'Truck',
     DESCRIPTION: 'Feature model of trucks used as default example in the Glencoe tool.',
     AUTHOR: 'Anna Schmitt et al.',
     YEAR: 2017,
     REFERENCE: 'https://ebooks.iospress.nl/volumearticle/49851',
     KEYWORDS: ['automotive', 'truck'],
     DOMAIN: 'automotive',
     FILENAME: 'Truck.uvl',
    },
    {NAME: 'JHipster v3.6.1',
     DESCRIPTION: 'A popular open-source code generator for web applications',
     AUTHOR: 'Axel Halin et al.',
     YEAR: 2017,
     REFERENCE: 'https://doi.org/10.1145/3023956.3023963',
     KEYWORDS: ['code generator', 'web'],
     DOMAIN: 'web applications',
     FILENAME: 'JHipster.uvl',
    },
    {NAME: 'GPL',
     DESCRIPTION: 'Standard SPL of classical graph applications that has been extensively used as a case study in the SPL community.',
     AUTHOR: 'Roberto E. Lopez-Herrejon & Don Batory',
     YEAR: 2001,
     REFERENCE: 'https://dl.acm.org/doi/10.5555/645418.652082',
     KEYWORDS: ['graph', 'search algorithm'],
     DOMAIN: 'graphs',
     FILENAME: 'GPL.xml',
    },
    {NAME: 'Tank War',
     DESCRIPTION: 'The feature model of a game implemented as an SPL with Feature-Oriented Programming.',
     AUTHOR: 'Lei Luo, Liang Liang, Songxuan Wu',
     YEAR: 2009,
     REFERENCE: 'http://spl2go.cs.ovgu.de/projects/7',
     KEYWORDS: ['game', 'tank', 'war'],
     DOMAIN: 'videogame',
     FILENAME: 'TankWar.xml',
    },
    {NAME: 'MobileMedia',
     DESCRIPTION: 'MobileMedia is a SPL for applications with about 3 KLOC that manipulate photo, music, and video on mobile devices.',
     AUTHOR: 'Eduardo Figueiredo et al.',
     YEAR: 2008,
     REFERENCE: 'https://doi.org/10.1145/1368088.1368124',
     KEYWORDS: ['media', 'mobile', 'phone', 'music', 'video', 'photo'],
     DOMAIN: 'mobile',
     FILENAME: 'MobileMedia.xml',
    },
    {NAME: 'WeaFQAs',
     DESCRIPTION: 'WeaFQAs is a software product line to manage the operationalizations of quality attributes.',
     AUTHOR: 'José Miguel Horcas et al.',
     YEAR: 2018,
     REFERENCE: 'https://hdl.handle.net/10630/17231',
     KEYWORDS: ['quality attribute', 'security', 'usability', 'persistence', 'energy consumption', 'performance'],
     DOMAIN: 'quality attributes',
     FILENAME: 'WeaFQAs.uvl',
    },
    {NAME: 'BusyBox 1.18.0-basic',
     DESCRIPTION: 'BusyBox is a command-line tool for Linux-based embedded systems that combines many standard shell commands in a single executable.',
     AUTHOR: 'Thorsten Berger et al.',
     YEAR: 2013,
     REFERENCE: 'https://doi.org/10.1109/TSE.2013.34',
     KEYWORDS: ['operating system', 'KConfig', 'Linux', 'command-line', 'shell'],
     DOMAIN: 'operating system',
     FILENAME: 'Busybox-1.18.0-basic.xml',
    },
    {NAME: 'Linux 2.6.33.3-basic',
     DESCRIPTION: 'Version of the Linux kernel FM in which pseudo-complex constraints have been converted into simple (requires and excludes) constraints.',
    AUTHOR: 'Alexander Knüppel et al.',
     YEAR: 2017,
     REFERENCE: 'https://doi.org/10.1145/3106237.3106252',
     KEYWORDS: ['operating system', 'KConfig', 'Linux', 'complex constraints'],
     DOMAIN: 'operating system',
     FILENAME: 'Linux-2.6.33.3-basic.uvl',
    },
     {NAME: 'Automotive 2.1-basic',
     DESCRIPTION: 'A version of the Automotive product line from an industrial partner.',
     AUTHOR: 'Alexander Knüppel et al.',
     YEAR: 2017,
     REFERENCE: 'https://doi.org/10.1145/3106237.3106252',
     KEYWORDS: ['industry', 'vehicle'],
     DOMAIN: 'automotive',
     FILENAME: 'Automotive2_1-basic.uvl',
    }
]