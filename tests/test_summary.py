import os

from ogc4_interface.plotting import plot_event_mcz_uncertainty
from ogc4_interface.summary import SUMMARY_FNAME, Summary


def test_summary(tmpdir):
    # if os.path.exists(SUMMARY_FNAME):
    #     os.remove(SUMMARY_FNAME)
    summary = Summary.load()  # via the OGC
    summary = Summary.load()  # via the cache
    assert len(summary) == 94
    # summary.download_data()
    ax = summary.plot()
    fig = ax.get_figure()
    fig.savefig(f"{tmpdir}/summary.png")
    fig, _ = plot_event_mcz_uncertainty(summary._data)
    fig.savefig(
        f"{tmpdir}/event_mcz_estimates.png", bbox_inches="tight", dpi=300
    )
