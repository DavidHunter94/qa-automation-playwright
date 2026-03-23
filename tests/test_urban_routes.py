import pytest
from playwright.sync_api import sync_playwright, expect
from pages.urban_routes_page import UrbanRoutesPage
import data


# -------------------------
# FIXTURES
# -------------------------

@pytest.fixture(scope="session")
def browser_context():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()
    pw.stop()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    page.goto(data.urban_routes_url)
    yield page
    page.close()


@pytest.fixture
def urban_routes_page(page):
    return UrbanRoutesPage(page)


# -------------------------
# TESTS
# -------------------------

class TestUrbanRoutes:

    def test_set_route(self, urban_routes_page):
        urban_routes_page.set_route(data.address_from, data.address_to)
        assert urban_routes_page.get_from() == data.address_from
        assert urban_routes_page.get_to() == data.address_to

    def test_select_plan(self, urban_routes_page, page):
        urban_routes_page.set_route(data.address_from, data.address_to)
        urban_routes_page.click_taxi_button()
        urban_routes_page.select_comfort_tariff()
        expect(page.locator(urban_routes_page.tarjeta_comfort_activa)).to_contain_text("Comfort")

    def test_fill_phone_number(self, urban_routes_page, page):
        urban_routes_page.set_route(data.address_from, data.address_to)
        urban_routes_page.click_taxi_button()
        urban_routes_page.select_comfort_tariff()
        urban_routes_page.fill_phone_and_verify()
        expect(page.locator(".np-text")).not_to_be_empty()

    def test_fill_credit_card(self, urban_routes_page, page):
        urban_routes_page.complete_basic_flow()
        expect(page.locator(".payment-picker")).not_to_be_visible()

    def test_comment_for_driver(self, urban_routes_page, page):
        urban_routes_page.complete_basic_flow()
        urban_routes_page.write_driver_message()
        expect(page.locator(urban_routes_page.message_field)).to_have_value(data.message_for_driver)

    def test_order_blanket_and_handkerchiefs(self, urban_routes_page, page):
        urban_routes_page.complete_basic_flow()
        urban_routes_page.request_blanket_and_tissues()
        expect(
            page.locator("//div[text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']")
        ).to_be_checked()

    def test_order_2_ice_creams(self, urban_routes_page, page):
        urban_routes_page.complete_basic_flow()
        urban_routes_page.request_ice_creams(2)
        expect(page.locator(urban_routes_page.counter_helado)).to_have_text("2")

    def test_car_search_model_appears(self, urban_routes_page, page):
        urban_routes_page.complete_basic_flow()
        urban_routes_page.write_driver_message()
        urban_routes_page.request_blanket_and_tissues()
        urban_routes_page.request_ice_creams(2)
        urban_routes_page.click_final_taxi_button()

        expect(page.locator(urban_routes_page.modal_titulo)).to_contain_text(
            "Buscar automóvil", timeout=30000
        )

    def test_full_order_flow(self, urban_routes_page, page):
        urban_routes_page.complete_basic_flow()
        urban_routes_page.write_driver_message()
        urban_routes_page.request_blanket_and_tissues()
        urban_routes_page.request_ice_creams(2)
        urban_routes_page.click_final_taxi_button()

        expect(page.locator(urban_routes_page.modal_titulo)).to_contain_text(
            "Buscar automóvil", timeout=30000
        )