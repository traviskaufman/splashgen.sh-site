from splashgen import launch
from splashgen.components import SplashSite, CTAButton

site = SplashSite(title="Splashgen - Landing Pages Built In Python",
                  theme="dark")
site.headline = "Travis Kaufman's Landing Page"
site.subtext = """
I'm a developer from NYC what up!
"""
site.call_to_action = CTAButton(
    "https://github.com/true3dco/splashgen", "View on GitHub")

launch(site)
