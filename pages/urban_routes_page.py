from playwright.sync_api import Page
import data

class UrbanRoutesPage:
    from_field = "#from"
    to_field = "#to"
    boton_taxi = "//button[text()='Pedir un taxi']"
    tarjeta_comfort = "//div[contains(@class,'tcard') and .//div[text()='Comfort']]"
    btn_phone = ".np-button"
    phone_input = "#phone"
    phone_code_input = "input[placeholder='xxxx']"
    boton_pago = ".pp-button.filled"
    fila_add_tarjeta = "//div[contains(@class,'pp-row') and .//div[text()='Agregar tarjeta']]"
    credit_card_number = "#number"
    credit_card_code = "//div[@class='card-code-input']//input"
    add_card_button = "//div[@class='pp-buttons']/button[normalize-space()='Agregar']"
    close_payment_modal = ".payment-picker .modal .close-button >> nth=0"
    blanket_switch = "//div[text()='Manta y pañuelos']/following-sibling::div//div[@class='switch']"
    plus_helado = "//div[text()='Helado']/following-sibling::div//div[contains(@class,'counter-plus')]"
    counter_helado = "//div[text()='Helado']/following-sibling::div//div[contains(@class,'counter-value')]"
    message_field = "#comment"
    boton_pedir_taxi_final = "button.smart-button"
    modal_titulo = ".order-header-title"
    tarjeta_comfort_activa = ".tcard.active .tcard-title"

    def __init__(self, page: Page):
        self.page = page
    def complete_basic_flow(self):
        self.set_route(data.address_from, data.address_to)
        self.click_taxi_button()
        self.select_comfort_tariff()
        self.fill_phone_and_verify()
        self.fill_credit_card()

    # -------------------------
    # ACCIONES
    # -------------------------
    def set_from(self, addr: str):
        self.page.locator(self.from_field).fill(addr)

    def set_to(self, addr: str):
        self.page.locator(self.to_field).fill(addr)

    def set_route(self, addr_from: str, addr_to: str):
        self.set_from(addr_from)
        self.set_to(addr_to)

    def get_from(self):
        return self.page.locator(self.from_field).input_value()

    def get_to(self):
        return self.page.locator(self.to_field).input_value()

    def click_taxi_button(self):
        self.page.locator(self.boton_taxi).click()

    def select_comfort_tariff(self):
        self.page.locator(self.tarjeta_comfort).click()

    def fill_phone_and_verify(self):
        self.page.locator(self.btn_phone).click()
        phone = self.page.locator(self.phone_input)
        phone.wait_for(state="visible")
        phone.fill(data.phone_number)

        with self.page.expect_response(
            lambda r: "api/v1/number?number" in r.url and r.status == 200
        ) as response_info:
            self.page.get_by_role("button", name="Siguiente").click()

        code = str(response_info.value.json().get("code", ""))

        if not code:
            raise Exception("Código no recibido")

        self.page.locator(self.phone_code_input).fill(code)
        self.page.get_by_role("button", name="Confirmar").click()

    def fill_credit_card(self):
        self.page.locator(self.boton_pago).click()
        self.page.locator(self.fila_add_tarjeta).click()
        self.page.locator(self.credit_card_number).fill(data.card_number)
        self.page.locator(self.credit_card_code).fill(data.card_code)
        self.page.keyboard.press("Tab")
        self.page.locator(self.add_card_button).click()
        self.page.locator(self.close_payment_modal).click(force=True)
        self.page.locator(".payment-picker.open").wait_for(state="hidden")

    # 🔥 CORREGIDO (locator específico + indentación correcta)
    def request_blanket_and_tissues(self):
        checkbox = self.page.locator(
            "//div[text()='Manta y pañuelos']/following-sibling::div//input[@type='checkbox']"
        )
        switch = self.page.locator(self.blanket_switch)

        switch.scroll_into_view_if_needed()

        if not checkbox.is_checked():
            switch.click()

    def request_ice_creams(self, count=2):
        plus = self.page.locator(self.plus_helado)
        for _ in range(count):
            plus.click()

    def write_driver_message(self):
        self.page.locator(self.message_field).fill(data.message_for_driver)

    def click_final_taxi_button(self):
        boton = self.page.locator(self.boton_pedir_taxi_final)
        boton.scroll_into_view_if_needed()
        boton.click()
