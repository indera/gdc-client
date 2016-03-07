GDC_API_HOST = 'gdc-api.nci.nih.gov'
GDC_API_PORT = 443

def config(parser):
    """ Configure an argparse parser for use with the GDC Client.
    """
    parser.add_argument('-H', '--host',
        default=GDC_API_HOST,
        help='GDC API host [{host}]'.format(host=GDC_API_HOST),
    )

    parser.add_argument('-P', '--port',
        default=GDC_API_PORT,
        help='GDC API port [{port}]'.format(port=GDC_API_PORT),
    )
