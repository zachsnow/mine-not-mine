#!/usr/bin/env python
import sys
import os.path
import subprocess
import codecs
import jinja2

PATH = os.path.dirname(os.path.abspath(__file__))
THEME_PATH = os.path.join(PATH, 'theme')
HTML = ['index.html']
OUTPUT_PATH = os.path.join(PATH, 'output')

SCSS_PATH = os.path.join(THEME_PATH, 'css/style.scss')
SCSS_OUTPUT_PATH = os.path.join(OUTPUT_PATH, 'style.css')
SCSS_ARGUMENTS = ['scss', '--style', 'expanded']

TEMPLATES_PATH = os.path.join(THEME_PATH, 'templates')

def css_filter(value):
    return value.lower()

loader = jinja2.FileSystemLoader([THEME_PATH, TEMPLATES_PATH])
env = jinja2.Environment(loader=loader)
env.filters.update({
    'css': css_filter,
})


def template(template_name, context):
    """
    Process the given `template` using the given `context`
    and return a string containing the output.
    """
    t = env.get_template(template_name)
    return t.render(**context)


def compile(input):
    """
    Compile the given SCSS and return a string containing
    the output.
    """
    args = []
    args.extend(SCSS_ARGUMENTS)
    args.extend([input, SCSS_OUTPUT_PATH])
    try:
        subprocess.check_output(args=args)
        with codecs.open(SCSS_OUTPUT_PATH, 'r', 'utf-8') as output:
            return output.read()
    except subprocess.CalledProcessError as e:
        print e.output
        return None


def save(filename, text):
    """
    Overwrite the file specified by `filename` with `text`.
    """
    with codecs.open(filename, 'w', 'utf-8') as file:
        file.write(text)


def main():
    css = compile(SCSS_PATH)
    if not css:
        raise Exception('unable to compile styles')
    
    for html in HTML:
        output = template(html, {
            'rendered_css': css
        })
        if not output:
            raise Exception('unable to render %s' % html)
        
        output_path = os.path.join(OUTPUT_PATH, html)
        save(output_path, output)


if __name__ == '__main__':
    try:
        main()
        print 'Done.'
        sys.exit(0)
    except Exception as e:
        print >> sys.stderr, 'Error: %s' % e
        print >> sys.stderr, 'Failed.'
        sys.exit(1)
