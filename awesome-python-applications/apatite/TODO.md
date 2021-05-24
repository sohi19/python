
# Fetching/pulling

* Fix outstanding git/hg/bzr clones, either with manual clone_urls or some other method (high pri)
  * solfege
  * sage
  * saleor
  * rhodecode
  * viewvc
  * gedit
* Add SVN support (low pri)
* Remove opsmop
* Establish the importance of libraries vs applications
  * The answers for applications differ from that of libraries'
* split out "assets" in sloc (xml, svg, json, yaml, qml)
  * maybe docs too? md, tex, rst, org
  * tooling: autoconf, make, meson, Dockerfile
* count python files
* update progress bar to say "(done)" instead of name of last project (wicd rn)
* tokei thinks .master = asp.net (also, ignore contrib, ignore vendor, ignore single files)

# Stats Ideas

* Hybridization / Co-occurrence with other languages (sloccount) (javascript, C, Cython, Java, etc.)
* Stars/forks (gh api, requires key) (also important for illustrating the contrast of scales in stars and collaboration)
* License (https://github.com/src-d/go-license-detector/releases)
* Packaging (containers: docker, snap, flatpak; freezers; setup.py/pypi, etc.)
* sloccount
* age / # of contributions, contributors. # of overlapping contributors.
* source control (git vs hg vs bzr)
* correlation between stars and contributors?
* Need to categorize small, medium, large
* Can committer distribution be used as an indicator of maturity?
* Can number of minor contributors be used as a proxy for popularity/usage?

## Architecture

* Server vs GUI vs CLI
* Django vs Flask vs Other Server
* Qt vs GTK vs TK vs Other GUI
* argparse vs click vs other CLI

# Data collection

* command to delete/archive results older than a certain date?
* load all results files
* apatite collect --targets --metrics
* apatite collate --date
* apatite analyze collated_file.json
* apatite-results__2019-08-10T10-10-10__2019-08-10T10-10-10.json (oldest date__newest_date)
* look at all targets for the collection, take the oldest and newest
  dates, then generate results filename, then start data collection
* collection needs to take into account existing valid results and resume
* for results collation, accept a date, load all results files with
  that date within their range, keep newest results up to that date
* apatite tarchive, apatite merge-tarchive ? (for cross-host results
  merging if repeating collection takes too long)
* sloc should be enhanced to create committer identities, grouped by
  case-/whitespace-normalized name and email.
* probably add metric name to results file? (faster collation, not an issue now)

## Licenses

Spotchecking the license output

* modoboa is actually ISC, not 0BSD (second guess)
* nvda is actually gplv2, under copying.txt (not bzip2)
* kallithea is actually GPLv3, not MPL
* 30 projects have no data (code is there for at least 15 of those)

# Collation

* Open all files with data between date ranges
* Scan through for unique combinations of supported metrics and still-listed projects
* Keep the most recent data (that isn't newer than the specified date)
  * isodates don't need to be parsed to be compared; stick to string comps for speed
* Future: Make note of which data is missing

# Tagsonomy improvements

* Console (and CLI/TUI/GUI) is more about UI than target platform

# Features

* Stale projects (have not been updated for more than X% of their lifespan)

# Interesting findings

* Even some older projects have already adopted asyncio. mailman, ipython, mitmproxy, even portage
* The weird hybrids. Haskell + Python (Ganeti, developed by google). Java + Python (nimbus, but 2014). Rust + Python (pants)
* One of the apps (Meson) has its own sloc type
* One app has all its docs written in TeX
* 90 tox.inis (I'm used to seeing tox for libraries, not applications)

<--! -->
