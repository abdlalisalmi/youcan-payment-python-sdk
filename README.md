<p  align="center"><a  href="https://youcanpay.com"  target="_blank"><img  src="https://youcanpay.com/images/ycpay-logo.svg"  width="400"></a></p>
<!--
<p align="center">
<a href="https://youcanpay.com"><img src="https://github.com/NextmediaMa/youcan-payment-php-sdk/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
<a href="https://packagist.org/packages/youcanpay/payment-sdk"><img src="https://img.shields.io/packagist/dt/youcanpay/payment-sdk" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/youcanpay/payment-sdk"><img src="https://img.shields.io/packagist/v/youcanpay/payment-sdk" alt="Latest Version"></a>
<a href="https://packagist.org/packages/youcanpay/payment-sdk"><img src="https://img.shields.io/packagist/l/youcanpay/payment-sdk" alt="License"></a>
</p>
-->

## [YouCan Pay & YouCan Pay Python SDK](#YouCan-Pay-&-YouCan-Pay-Python-SDK)

YouCan Pay is a payment platform initially developed to solve the payment gateway issue for e-merchants, And it's a simple way to accept timely payments online. You can use a Moroccan or international credit card to transfer money from a customer's bank account to yours.
YouCan Pay Python SDK is a Python package that allows the developers to interact easily with the [YouCan Pay API](https://youcanpay.com/docs).

### Summary

- [YouCan Pay & YouCan Pay Python SDK](#YouCan-Pay-&-YouCan-Pay-Python-SDK)
- [Why](#Why)
  - [Why not use the YouCan Pay API directly?](#Why-not-use-the-YouCan-Pay-API-directly?)
- [YouCan Pay SDK Setup](#YouCan-Pay-SDK-Setup)
  - [Requirements](#Requirements)
  - [Installation](#Installation)
- [Integration](#Integration)
  - [YouCan Pay: Default Integration](#1.-YouCan-Pay:-Default-Integration)

## [Why not use the YouCan Pay API directly?](#Why-not-use-the-YouCan-Pay-API-directly?)

Using the SDK can simplify and speed up the development process, and ensure that your application is using the API in a consistent and maintainable manner. And can provide several benefits over using the API alone:

- **Streamlined development process:** SDKs often include pre-built components and integrations that simplify the development process, saving you time and effort compared to building everything from scratch using just the API.

- **Higher-level abstractions:** SDKs can provide higher-level abstractions that abstract away some of the low-level details of working with the API, making it easier to build complex applications.

- **Better documentation:** SDKs typically include documentation that is specific to the SDK, which can be more detailed and easier to understand than the general API documentation.

- **Consistency:** Using an SDK ensures that your application is using the API in a consistent manner across all parts of the application.

- **Easier maintenance:** Because an SDK typically includes pre-built components and abstractions, it can be easier to maintain and update your application when changes are made to the underlying API.

## [YouCan Pay SDK Setup](#YouCan-Pay-SDK-Setup)

Instructions for adding the YouCan Pay SDK to your Python Application.

#### [Requirements](#Requirements)

- YouCan Pay Account.
- Your YouCan Pay `private_key` and `public_key` available in Settings > API Keys.
- This package installed in your Development / Production environment.

#### [Installation](#Installation)

Open your Python project, add the following.

```bash
Coming Soon... (or for now you can use the source code)
```

## [Integration](#Integration)

#### [1. YouCan Pay: Default Integration](#1.-YouCan-Pay:-Default-Integration)

You can make payments directly on your site, with the possibility of choosing the position in the DOM.
If you choose to use JS integration (Default Integration), keep in mind that you must have an SSL certificate to run in production mode.

1.1: Copy this JS script between `<head>...</head>`

```javascript
<script src="https://pay.youcan.shop/js/ycpay.js"></script>
```

1.2: Choose where you want to display payment information (Full Name, Card Numbers, CCV...), must be placed between the `<body>...</body>` tags.

```javascript
<div id="payment-card"></div> // the div that will contain the payment form
<div id="error-container"></div> // the div that will contain the errors
<button id="pay">Pay</button> // the button that will trigger the payment
```

1.3: Add this code just before the end of the `...</body>` tag.

```javascript
<script type="text/javascript">
  // Create a YouCan Pay instance.
  const ycPay = new YCPay(
    // String public_key (required): Login to your account.
    // Go to Settings and open API Keys and copy your key.
    "public_key",
    // Optional options object
    {
      formContainer: "#payment-card",
      // Defines what language the form should be rendered in, supports EN, AR, FR.
      locale: "en",

      // Whether the integration should run in sandbox (test) mode or live mode.
      isSandbox: false,

      // A DOM selector representing which component errors should be injected into.
      // If you omit this option, you may alternatively handle errors by chaining a .catch()
      // On the pay method.
      errorContainer: "#error-container",
    }
  );

  // Select which gateways to render
  ycPay.renderAvailableGateways(["CashPlus", "CreditCard"]);

  // Alternatively, you may use gateway specific render methods if you only need one.
  ycPay.renderCreditCardForm();
</script>
```

1.4: Tokenization: generate a token to use it in the payment process.

```python
from youcanpay import YouCanPay

# Initialize the SDK instance
# You can use the sandbox mode to test the integration.
# Sandbox mode is set to False by default.
youcanpay =  YouCanPay(private_key='pri_**', public_key='pub_**', sandbox_mode=True)

# Data of the customer who wishes to make this purchase.
# Please keep these keys.
customer_info = {
		'name': '',
		'address':'',
		'zip_code': '',
		'city': '',
		'state': '',
		'country_code': '',
		'phone': '',
		'email': '',
	 }

# You can use it to send data to retrieve after the response or in the webhook.
metadata = {
	# Can you insert what you want here...
	'key': 'value'
}

# Create a token.
token = youcanpay.token.create(
		#String orderId (required): Identifier of the order you want to be paid.
		orderId="123456789",
		# Integer amount (required): The amount, Example: 25 USD is 2500.
		amount=100,
		# String currency (required): Uppercase currency.
		currency="MAD"
		# String customerIP (required): Customer Address IP.
		customer_ip="123.123.123.123",
		# String successUrl (required): This URL is returned when the payment is successfully processed.
		success_url = "https://yourdomain.com/orders-status/success",
		# String errorUrl (required): This URL is returned when payment is invalid.
		error_url = "https://yourdomain.com/orders-status/error",
		# Array customerInfo (optional): Data of the customer who wishes to make this purchase.
		customer_info = customer_info,
		# Array metadata (optional): You can use it to send data to retrieve after the response or in the webhook.
		metadata= metadata
	)
print(token.id) #>> ac7dcb21-f871-6612-88c6-551e9ad2132f
```

1.5: Retrieve the token you created with the SDK in your **backend** and insert it into the JS script, this token which contains all the information concerning this payment.

When the buyer clicks on the Pay button. the JS code below runs, and you receive a **GET** response in **successUrl** or **errorUrl** you defined in the tokenization step.

```javascript
<script type="text/javascript">
  // Start the payment on button click
  document.getElementById("pay").addEventListener("click", function () {
    // Execute the payment, it is required to put the created token in the tokenization step.
    ycPay
      .pay("token_id")
      .then(successCallback)
      .catch(errorCallback);
  });

  function successCallback(transactionId) {
    //your code here
  }

  function errorCallback(errorMessage) {
    //your code here
  }
</script>
```

<!-- #### [Initialize the SDK](#Initialize-the-SDK)

```python
from youcanpay import YouCanPay

# Initialize the SDK instance
youcanpay =  YouCanPay(private_key='pri_**', public_key='pub_**', sandbox_mode=True)
```

#### [Keys](#Keys)

Keys it's a class that contains all the methods related to the API Keys.

- **[Keys.check()](<#Keys.check()>):**
  Check if the keys are valid or not.

  ```python
  # Check the keys if is valid or not.
  youcanpay.keys.check()
  ```

#### [Token](#Token)

Token it's a class that contains all the methods related to the **payment token**.

- **[Token.create():](<#Token.create()>):**
  Generating a payment token to use it in the payment process.

  ```python
  # Create a token.
  token = youcanpay.token.create(
  		orderId="123456789", # Required
  		amount=100, # Required
  		currency="MAD" # Required
  		success_url = None, # Optional
  		error_url = None, # Optional
  		customer_ip="127.0.0.1", # Optional
  		customer_info = [], # Optional
  		metadata= [] # Optional
  	)
  print(token.id) #>> ac7dcb21-f871-6612-88c6-551e9ad2132f
  ``` -->
