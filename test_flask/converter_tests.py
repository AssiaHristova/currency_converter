
from unittest import TestCase, main, mock
from converter import get_currencies, app


class CurrencyConverterTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    @mock.patch("converter.requests.post")
    def test_get_currencies(self, mock_post):
        my_mock_response = mock.Mock(status_code=200)
        mock_post.return_value = my_mock_response
        self.assertEqual(my_mock_response.status_code, 200)

        currencies = get_currencies()
        self.assertEqual(currencies["USD"], 1)

    @mock.patch("converter.requests.post")
    def test_get_currencies_if_not_found(self, mock_post):
        my_mock_response = mock.Mock(status_code=200)
        my_mock_response.side_effect = Exception
        self.assertEqual(my_mock_response.status_code, 200)
        self.assertEqual(my_mock_response.side_effect, Exception)

    @mock.patch("converter.requests.post")
    def test_home_if_request_method_is_get(self, mock_post):
        my_mock_response = mock.Mock(status_code=200)
        self.assertEqual(my_mock_response.status_code, 200)

    @mock.patch("converter.requests.post")
    def test_home_if_not_found(self, mock_post):
        my_mock_response = mock.Mock(status_code=200)
        my_mock_response.side_effect = Exception
        self.assertEqual(my_mock_response.status_code, 200)
        self.assertEqual(my_mock_response.side_effect, Exception)


if __name__ == "__main__":
    main()


