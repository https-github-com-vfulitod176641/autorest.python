import os
from invoke import task

default_mappings = {
  'AcceptanceTests/AdditionalProperties': 'additionalProperties.json',
  'AcceptanceTests/ParameterFlattening': 'parameter-flattening.json',
  'AcceptanceTests/BodyArray': 'body-array.json',
  'AcceptanceTests/BodyBoolean': 'body-boolean.json',
  'AcceptanceTests/BodyByte': 'body-byte.json',
  'AcceptanceTests/BodyComplex': 'body-complex.json',
  'AcceptanceTests/BodyDate': 'body-date.json',
  'AcceptanceTests/BodyDateTime': 'body-datetime.json',
  'AcceptanceTests/BodyDateTimeRfc1123': 'body-datetime-rfc1123.json',
  'AcceptanceTests/BodyDuration': 'body-duration.json',
  'AcceptanceTests/BodyDictionary': 'body-dictionary.json',
  'AcceptanceTests/BodyFile': 'body-file.json',
  'AcceptanceTests/BodyFormData': 'body-formdata.json',
  'AcceptanceTests/BodyInteger': 'body-integer.json',
  'AcceptanceTests/BodyNumber': 'body-number.json',
  'AcceptanceTests/BodyString': 'body-string.json',
  'AcceptanceTests/ExtensibleEnums': 'extensible-enums-swagger.json',
  'AcceptanceTests/Header': 'header.json',
  'AcceptanceTests/Http': 'httpInfrastructure.json',
  'AcceptanceTests/Report': 'report.json',
  'AcceptanceTests/RequiredOptional': 'required-optional.json',
  'AcceptanceTests/Url': 'url.json',
  'AcceptanceTests/Validation': 'validation.json',
  'AcceptanceTests/CustomBaseUri': 'custom-baseUrl.json',
  'AcceptanceTests/CustomBaseUriMoreOptions': 'custom-baseUrl-more-options.json',
  'AcceptanceTests/ModelFlattening': 'model-flattening.json',
  'AcceptanceTests/Xml': 'xml-service.json',
  'AcceptanceTests/UrlMultiCollectionFormat' : 'url-multi-collectionFormat.json'
}

default_azure_mappings = {
  'AcceptanceTests/AzureBodyDuration': 'body-duration.json',
  'AcceptanceTests/AzureReport': 'azure-report.json',
  'AcceptanceTests/AzureParameterGrouping': 'azure-parameter-grouping.json',
  'AcceptanceTests/ModelFlattening': 'model-flattening.json',
  'AcceptanceTests/CustomBaseUri': 'custom-baseUrl.json'
}

# The list is mostly built on Swaggers that uses CloudError feature
# These Swagger should be modified to test their features, and not the CloudError one
default_arm_mappings = {
  'AcceptanceTests/Head': 'head.json',
  'AcceptanceTests/HeadExceptions': 'head-exceptions.json',
  'AcceptanceTests/StorageManagementClient': 'storage.json',
  'AcceptanceTests/Lro': 'lro.json',
  'AcceptanceTests/SubscriptionIdApiVersion': 'subscriptionId-apiVersion.json',
  'AcceptanceTests/Paging': 'paging.json',
  'AcceptanceTests/AzureSpecials': 'azure-special-properties.json',
}

base_dir = os.path.dirname(__file__)

swagger_dir = "node_modules/@microsoft.azure/autorest.testserver/swagger"


@task
def regen_expected(c, opts):
    output_dir = "{}/{}".format(opts['output_base_dir'], opts['output_dir']) if opts.get('output_base_dir') else opts['output_dir']
    keys = opts['mappings'].keys()
    instances = len(keys)

    for key in keys:
        opts_mappings_value = opts['mappings'][key]
        key = key.strip();

        swagger_files = (opts_mappings_value[0] if isinstance(opts_mappings_value, list) else opts_mappings_value).split(';')
        args = [
            "--use={}".format(base_dir),
            "--{}".format(opts['language']),
            "--clear-output-folder",
            "--output-folder={}/{}".format(output_dir, key),
            "--license-header={}".format(opts['header'] if opts.get('header') else 'MICROSOFT_MIT_NO_VERSION'),
            "--enable-xml",
            "--basic-setup-py",
            "--trace"
        ]

        for swagger_file in swagger_files:
            input_file_name = "{}/{}".format(opts['input_base_dir'], swagger_file) if opts.get('input_base_dir') else swagger_file
            args.append("--input-file={}".format(input_file_name))

        if opts.get('add_credentials') and opts['add_credentials']:
            args.append("--{}.add-credentials=true".opts['language'])

        if opts.get('vanilla') and opts['vanilla']:
            args.append("--{}.vanilla=true".format(opts['language']))

        if opts.get('azure_arm') and opts['azure_arm']:
            args.append("--{}.azure-arm=true".format(opts['language']))

        if opts.get('flattening_threshold'):
            args.append("--{}.payload-flattening-threshold={}".format(opts['language'], opts['flattening_threshold']))

        if opts.get('keep_version') and opts['keep_version']:
            args.append("--{}.keep-version-file=true".format(opts['language']))

        if opts.get('ns_prefix'):
            if isinstance(opts_mappings_value, list) and len(opts_mappings_value) > 1:
                args.append("--{}.namespace={}".format(opts['language'], opts_mappings_value[1]))
            else:
                namespace = [opts['ns_prefix'], key.replace("/\/|\./", '')].join('.')
                args.append("--{}.namespace={}".format(opts['language'], namespace))

        if opts.get('override-info.version'):
            args.append("--override-info.version={}".format(opts['override-info.version']))
        if opts.get('override-info.title'):
            args.append("--override-info.title={}".format(opts['override-info.title']))
        if opts.get('override-info.description'):
            args.append("--override-info.description={}".format(opts['override-info.description']))

        c.run('echo Queuing up: Autorest {}'.format(" ".join(args)))
        c.run('{}/node_modules/.bin/autorest {}'.format(base_dir, " ".join(args)))
        instances -= 1
        if not instances:
            return


@task
def regenerate_python(c):
    opts = {
        'output_base_dir': 'test/vanilla',
        'input_base_dir': swagger_dir,
        'mappings': default_mappings,
        'output_dir': 'Expected',
        'language': 'python',
        'flattening_threshold': '1',
        'vanilla': True,
        'keep_version': True
    }
    regen_expected(c, opts)


@task
def regenerate_python_azure(c):
    opts = {
        'output_base_dir': 'test/azure',
        'input_base_dir': swagger_dir,
        'mappings': default_azure_mappings,
        'output_dir': 'Expected',
        'language': 'python',
        'flattening_threshold': '1'
    }
    regen_expected(c, opts)


@task
def regenerate_python_arm(c):
    opts = {
        'output_base_dir': 'test/azure',
        'input_base_dir': swagger_dir,
        'mappings': default_arm_mappings,
        'output_dir': 'Expected',
        'language': 'python',
        'azure_arm': True,
        'flattening_threshold': '1'
    }
    regen_expected(c, opts)


@task
def regenerate(c):
    # regenerate expected code for tests
    regenerate_python(c)
    regenerate_python_azure(c)
    regenerate_python_arm(c)


@task
def test(c):
    # run language-specific tests
    os.chdir("{}/test/vanilla/".format(base_dir))
    c.run('tox')
    os.chdir("{}/test/azure/".format(base_dir))
    c.run('tox')