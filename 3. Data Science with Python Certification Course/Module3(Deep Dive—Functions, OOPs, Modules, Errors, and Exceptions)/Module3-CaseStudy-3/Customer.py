{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNrPTihQ075dMuR2IixAlSz"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":1,"metadata":{"colab":{"base_uri":"https://localhost:8080/","height":373},"id":"fG0dTAc6VCTi","executionInfo":{"status":"error","timestamp":1668081515702,"user_tz":-330,"elapsed":656,"user":{"displayName":"Prasanth Kumar","userId":"05338423061206619181"}},"outputId":"30ea6a03-af21-4665-9602-d1f5d60b8e2e"},"outputs":[{"output_type":"error","ename":"ModuleNotFoundError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)","\u001b[0;32m<ipython-input-1-de993f6b69a6>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mOrder\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mCustomerNotAllowedException\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mclass\u001b[0m \u001b[0mCustomer\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'Order'","","\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"],"errorDetails":{"actions":[{"action":"open_url","actionText":"Open Examples","url":"/notebooks/snippets/importing_libraries.ipynb"}]}}],"source":["import Order\n","import CustomerNotAllowedException\n","\n","\n","class Customer:\n","    def __init__(self, productname, customername, isblacklisted):\n","        self.productname = productname\n","        self.customername = customername\n","        self.isblacklisted = isblacklisted\n","\n","    def createOrder(self, productname, productcode):\n","        if self.isblacklisted:\n","            raise CustomerNotAllowedException(\n","                \"Customer is not allowed to create the order because it is blacklisted.\")\n","\n","        order = Order(productname, productcode)\n","\n","        return order"]}]}