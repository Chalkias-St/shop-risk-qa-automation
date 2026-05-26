import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        yield page

        if request.node.rep_call.failed:
            page.screenshot(path=f"screenshots/{request.node.name}.png")

            context.tracing.stop(
                path=f"traces/{request.node.name}.zip"
            )
        else:
            context.tracing.stop()

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)