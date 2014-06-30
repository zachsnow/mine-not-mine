# Mine / Not Mine

**Mine / Not Mine** is the Tumblr theme for [Gathered By The Way](http://gatheredbytheway.com/),
gatherings from the daily life of the Travelling Designer, Anthony Cappetta.
It was made by [Zach Snow](http://zachsnow.com/).

**Note** If you just want to use the theme as-is, simply download the
[main theme](https://github.com/zachsnow/mine-not-mine/tree/master/output/index.html).
For instructions on how to install these files, see [Installation](#installation),
below.

## <a name="dependencies"></a>Dependencies

To build the theme manually -- for instance, if you'd like to tweak
it -- you'll need to install the following dependencies:

  * [Sass](http://sass-lang.com/)
  * [Jinja2](http://www.pocoo.org/projects/jinja2/#jinja2)

Assuming you are running OS X and have [Homebrew](http://mxcl.github.com/homebrew/) and
[Pip](http://www.pip-installer.org/en/latest/) installed, you should
be able to simply run the following:

    $ brew install sass
    $ pip install jinja2

Assuming you don't you'll have to sort it out yourself.

## <a name="building"></a>Building

To build the theme first make sure you've installed all of the
[Dependencies](#dependencies). Then, run the following command from the
root of this repository.

    $ python build.py
    
This will generate `output/index.html`.

## <a name="installation"></a>Installing

Once you have `index.html` in hand, you just
need to install them on [Tumblr](http://tumblr.com). Login to Tumblr
and go to **Settings**. Select the blog you'd like to edit from the left
column, then click **Customize**.

First you need to setup your main theme. Click **Edit HTML** and overwrite
the existing HTML with the contents of `index.html`, then **Update Preview**
to see how it looks. Assuming you are happy with the result, **Save** it.

## <a name="configuring"></a>Configuring

Now that the theme is installed, you need to configure it.  The colors
are pretty obvious, but here's some information about the rest.

### Logo

Add a logo. It should be some number of pixels wide that I don't know yet.

### Navigation

You can add up to 10 external navigation links to the header navigation
by setting `Navigation N` and `Navigation Link N` for `1` to `10`, where
the former corresponds to the text of the link, and the latter the actual
URL.

### Byline

The `Byline` settings change how the footer looks.  In the example
at [that's me](http://therealzachsnow.tumblr.com) the `Byline Prefix`
is set to "Theme by", the `Byline` is set to "Zach Snow", and the
`Byline Link` is set to "[http://zachsnow.com/](http://zachsnow.com/)".
If you want, you can use a `mailto:` link.  And if you don't want a link
at all, just don't set `Byline Link`. In fact, all of the `Byline` settings
are optional.

### Social Media

You can add links for a handful of different social media platforms;
these are shown in the footer as well.

### Google Analytics

Google Analytics integration is as per usual, just grab your account
ID and set `Google Analytics ID`.

### Typekit

There are two customizable Typekit fonts, one for headers and one for
all the rest of the text. To set these up, first create a new kit and
grab the kit "identifier" (the basename of the embed code Javascript file)
and set `Typekit ID`.

Next, pick your fonts, and set `Typkit Header Font Family` and `Typekit Text Font Family`
to whichever font families you picked. Of course, you can add all kinds of
other selectors to your kit too, if you want to get crazy.
