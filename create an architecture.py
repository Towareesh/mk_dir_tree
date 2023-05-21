import os
import logging


logging.basicConfig(level=logging.INFO)

def decay_catalog_tree(catalog_tree: dict) -> tuple:
    # return root_catalog and subdirectories

    root_catalog   = list(catalog_tree.keys())[0]
    subdirectories = [subdir for subdir in catalog_tree[root_catalog]]
    return root_catalog, subdirectories
    

def create_dir_tree(root_catalog: str, subdirs: list) -> None:
    """Recursive create catalogs tree.
    
    Subdirs can contain a tree of subdirectories,
    these will be nested dictionaries,
    the values of which must necessarily be lists.

    If root subdirs contains,
    dictionary must be decompose at dir name and subdirs.

    Example:
        root_catalog - 'app'
        subdirs - [{'temp': ['sub_temp', {'sub_sub_temp': ['test']}]},
                    'main',
                    'static']

    Args:
        root_catalog (str): Name root catalog
        subdirs (list): Сonstruction of list and nested dictionaries
    """

    if not os.path.exists(root_catalog):
        os.mkdir(root_catalog)
        logging.info(f'Created catalog: {root_catalog}')

    for subdir in subdirs:
        if isinstance(subdir, dict):
            decay_catalog = decay_catalog_tree(subdir)
            subdir_root_name    = decay_catalog[0]
            subdir_root_subdirs = decay_catalog[1]
            create_dir_tree(f'{root_catalog}/{subdir_root_name}',
                           subdir_root_subdirs)

        elif not os.path.exists(f'{root_catalog}/{subdir}'):
            os.mkdir(f'{root_catalog}/{subdir}')
            logging.info(f'Created subcatalog: {root_catalog}/{subdir}')


# config_catalogs = {'root': 'repair_flask_pj',
#                    'subdirs': [{'app': ['auth',
#                                         'errors',
#                                         'main',
#                                         'static',
#                                         {'templates': ['auth',
#                                                        'email',
#                                                        'errors']}]},
#                                'flaskenv',
#                                'appDB',
#                                'conf_tarnslate',
#                                'pytests']}


# create_dir_tree(config_catalogs['root'], config_catalogs['subdirs'])