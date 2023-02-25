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
- [Setup](#Setup)
- [Documentation](#Documentation)
  - [Initialize the SDK](#Initialize-the-SDK)
  - [Keys](#Keys)

## [Why not use the YouCan Pay API directly?](#Why-not-use-the-YouCan-Pay-API-directly?)

Using the SDK can simplify and speed up the development process, and ensure that your application is using the API in a consistent and maintainable manner. And can provide several benefits over using the API alone:

- **Streamlined development process:** SDKs often include pre-built components and integrations that simplify the development process, saving you time and effort compared to building everything from scratch using just the API.

- **Higher-level abstractions:** SDKs can provide higher-level abstractions that abstract away some of the low-level details of working with the API, making it easier to build complex applications.

- **Better documentation:** SDKs typically include documentation that is specific to the SDK, which can be more detailed and easier to understand than the general API documentation.

- **Consistency:** Using an SDK ensures that your application is using the API in a consistent manner across all parts of the application.

- **Easier maintenance:** Because an SDK typically includes pre-built components and abstractions, it can be easier to maintain and update your application when changes are made to the underlying API.

## [Setup](#Setup)

Instructions for adding the YouCan Pay SDK to your Python Application.

#### Step 1: Requirements

- YouCan Pay Account.
- Your YouCan Pay `private_key` and `public_key` available in Settings > API Keys.
- This package installed in your Development / Production environment.

#### Step 2: Installation

Open your Python project, add the following.

```bash
Coming Soon... (or for now you can use the source code)
```

## [Documentation](#Documentation)

#### [Initialize the SDK](#Initialize-the-SDK)

```python
from youcanpay import YouCanPay

# Initialize the SDK instance
youcanpay =  YouCanPay(private_key='pri_**', public_key='pub_**', sandbox_mode=True)
```

#### [Keys](#Keys)

Check the keys if is valid or not with `.check()` method.

```python
# Check the keys if is valid or not.
youcanpay.keys.check()
```

#### [Token](#Token)

Create a token with `.create()` method.

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
```

<!---
##### Step 2.1: YouCan Pay: Default Integration
If you choose to use JS integration, you must have an SSL certificate to run in production mode.

2.1.1: Copy this JS script between  `<head>...</head>`
```javascript
<script src="https://pay.youcan.shop/js/ycpay.js"></script>
```
2.1.2: Choose where you want to display payment information (Full Name, Card Numbers, CCV...), must be placed between the `<body>...</body>` tags.
```javascript
<div id="payment-card"></div>
<button id="pay">Pay</button>
```
2.1.3: Add this code just before the end of the `...</body>` tag.
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

-->
