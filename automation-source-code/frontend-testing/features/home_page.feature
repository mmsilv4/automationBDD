Feature:  Home Page


    @login
    Background: Login 
        Given The login was successful with user and password
        When  The home screen is displdayed 


    Scenario: HS_01 - Verify that the menu is displayed as expected
        Given I am on home screen
        Then  I verify that the menu options are accordin the following data
            | menu_value       |
            | Meu Painel       |
            | Perfil de Beleza |
            | Glampoints       |
            | Comunidade       |
            | Conteúdo         |
            | Ajuda            |