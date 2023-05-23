"""This is a template for Auto-GPT plugins."""
import abc
from typing import Any, Dict, List, Optional, Tuple, TypeVar, TypedDict, Union
from .trade import Trade
from .market import Market
from .account import Account
from .lab import Lab

from abstract_singleton import AbstractSingleton, Singleton

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class AutoGPTOandaPlugin(AbstractSingleton, metaclass=Singleton):
    """
    This is a plugin to use Auto-GPT with OANDA API.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-OANDA-Plugin"
        self._version = "0.1.0"
        self._description = "This is a plugin to use Auto-GPT with OANDA API."

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.

        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.

        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return False

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        """This method is called just after the generate_prompt is called,
            but actually before the prompt is generated.

        Args:
            prompt (PromptGenerator): The prompt generator.

        Returns:
            PromptGenerator: The prompt generator.
        """
        # Trade
        prompt.add_command(
            "Create Order",
            "order_create",
            {
                "instrument": "<instrument>",
                "price": "<price>",
                "stop_loss": "<stop_loss>",
                "take_profit": "<take_profit>",
                "units": "<units>",
                "type": "<type>",
            },
            self.order_create
        )
        prompt.add_command(
            "Cancel Order",
            "order_cancel",
            {
                "order_id": "<order_id>",
            },
            self.order_cancel
        )
        prompt.add_command(
            "Get Order Details",
            "order_details",
            {
                "order_id": "<order_id>",
            },
            self.order_details
        )
        prompt.add_command(
            "Get Order List",
            "order_list",
            {},
            self.order_list
        )
        prompt.add_command(
            "Close Trade",
            "trade_close",
            {
                "trade_id": "<trade_id>",
                "units": "<units>",
            },
            self.trade_close
        )
        prompt.add_command(
            "Get Trade Details",
            "trade_details",
            {
                "trade_id": "<trade_id>",
            },
            self.trade_details
        )
        prompt.add_command(
            "Get Trades List",
            "trades_list",
            {
                "instruments": "<instruments>",
            },
            self.trades_list
        )
        prompt.add_command(
            "Close Position",
            "position_close",
            {
                "instrument": "<instrument>",
                "longUnits": "<longUnits>",
                "shortUnits": "<shortUnits>",
            },
            self.position_close
        )
        prompt.add_command(
            "Get Position Details",
            "position_details",
            {
                "instrument": "<instrument>",
            },
            self.position_details
        )
        prompt.add_command(
            "Position List",
            "position_list",
            {
            },
            self.position_list
        )
        # Market
        prompt.add_command(
            "Get Instruments Candles",
            "instruments_candles",
            {
                "instrument": "<instrument>",
                "granularity": "<granularity>",
                "count": "<count>",
            },
            self.instruments_candles
        )
        # Account
        prompt.add_command(
            "Get Account Summary",
            "get_account_summary",
            {
            },
            self.get_account_summary
        )
        prompt.add_command(
            "Get Account Instruments",
            "get_account_instruments",
            {
                "instruments": "<instruments>"
            },
            self.get_account_instruments
        )
        # Lab
        prompt.add_command(
            "Get Autochartist Data",
            "autochartist",
            {
                "instrument": "<instrument>",
            },
            self.autochartist,
        )
        prompt.add_command(
            "Get Calendar",
            "calendar",
            {
                "instrument": "<instrument>",
                "period": "<period>",
            },
            self.calendar,
        )
        prompt.add_command(
            "Get Commitments of Traders",
            "commitments_of_traders",
            {
                "instrument": "<instrument>",
            },
            self.commitments_of_traders,
        )
        prompt.add_command(
            "Get Historical Position Ratios",
            "historical_position_ratios",
            {
                "instrument": "<instrument>",
                "period": "<period>",
            },
            self.historical_position_ratios,
        )
        prompt.add_command(
            "Get Orderbook Data",
            "orderbook_data",
            {
                "instrument": "<instrument>",
                "period": "<period>",
            },
            self.orderbook_data,
        )
        prompt.add_command(
            "Get Spreads",
            "spreads",
            {
                "instrument": "<instrument>",
                "period": "<period>",
            },
            self.spreads,
        )
        
        return prompt

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.

        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.

        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.

        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.

        Args:
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.

        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.

        Args:
            messages (List[Message]): The list of context messages.

        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.

        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.

        Args:
            messages (List[Message]): The list of context messages.

        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.

        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.

        Args:
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.

        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.

        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.

        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.

        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.

        Args:
            command_name (str): The command name.
            response (str): The response.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.

        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.

          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.

        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.

        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_text_embedding(
        self, text: str
    ) -> bool:
        """This method is called to check that the plugin can
          handle the text_embedding method.
        Args:
            text (str): The text to be convert to embedding.
          Returns:
              bool: True if the plugin can handle the text_embedding method."""
        return False
    
    def handle_text_embedding(
        self, text: str
    ) -> list:
        """This method is called when the chat completion is done.
        Args:
            text (str): The text to be convert to embedding.
        Returns:
            list: The text embedding.
        """
        pass

    def can_handle_user_input(self, user_input: str) -> bool:
        """This method is called to check that the plugin can
        handle the user_input method.

        Args:
            user_input (str): The user input.

        Returns:
            bool: True if the plugin can handle the user_input method."""
        return False

    def user_input(self, user_input: str) -> str:
        """This method is called to request user input to the user.

        Args:
            user_input (str): The question or prompt to ask the user.

        Returns:
            str: The user input.
        """

        pass

    def can_handle_report(self) -> bool:
        """This method is called to check that the plugin can
        handle the report method.

        Returns:
            bool: True if the plugin can handle the report method."""
        return False

    def report(self, message: str) -> None:
        """This method is called to report a message to the user.

        Args:
            message (str): The message to report.
        """
        pass
    
    def order_create(
        self, 
        instrument: str,
        price: float,
        stop_loss: float,
        take_profit: float,
        units: float,
        type: str,
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.order_create(
            instrument=instrument,
            price=price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            units=units,
            type=type,
        )
        return data

    def order_cancel(
        self, 
        order_id: str,
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.order_cancel(order_id)
        return data
    
    def order_details(
        self,
        order_id: str,
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.order_details(order_id)
        return data
    
    def order_list(
        self
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.order_list()
        return data
    
    def trade_close(
        self, 
        trade_id: str,
        units: float
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.trade_close(trade_id, units)
        return data
    
    def trade_details(
        self,
        trade_id: str,
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.trade_details(trade_id)
        return data
    
    def trades_list(
        self,
        instruments: str
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.trades_list(instruments)
        return data
    
    def position_close(
        self, 
        instrument: str,
        longUnits: Optional[Union[int,str]],
        shortUnits: Optional[Union[int,str]],
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.position_close(instrument, longUnits, shortUnits)
        return data
    
    def position_details(
        self,
        instrument: str,
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.position_details(instrument)
        return data
    
    def position_list(
        self
    ) -> Optional[Dict[str, Any]]:
        trade = Trade()
        data = trade.position_list()
        return data
    
    def instruments_candles(
        self,
        instrument: str,
        granularity: str,
        count: int
    ) -> Optional[Dict[str, Any]]:
        market = Market()
        data = market.instruments_candles(instrument, granularity, count)
        return data
    
    def get_account_summary(
        self
    ) -> Optional[Dict[str, Any]]:
        account = Account()
        data = account.get_account_summary()
        return data
    
    def get_account_instruments(
        self,
        instruments: str
    ) -> Optional[Dict[str, Any]]:
        account = Account()
        data = account.get_account_instruments(instruments)
        return data
    
    def autochartist(
        self,
        instrument: str,
    ) -> Optional[Dict[str, Any]]:
        lab = Lab()
        data = lab.autochartist(instrument)
        return data
    
    def calendar(
        self,
        instrument: str,
        period: str,
    ) -> Optional[Dict[str, Any]]:
        lab = Lab()
        data = lab.calendar(instrument, period)
        return data
    
    def commitments_of_traders(
        self,
        instrument: str,
    ) -> Optional[Dict[str, Any]]:
        lab = Lab()
        data = lab.commitments_of_traders(instrument)
        return data
    
    def historical_position_ratios(
        self,
        instrument: str,
        period: str,
    ) -> Optional[Dict[str, Any]]:
        lab = Lab()
        data = lab.historical_position_ratios(instrument, period)
        return data
    
    def orderbook_data(
        self,
        instrument: str,
        period: str,
    ) -> Optional[Dict[str, Any]]:
        lab = Lab()
        data = lab.orderbook_data(instrument, period)
        return data
    
    def spreads(
        self,
        instrument: str,
        period: str,
    ) -> Optional[Dict[str, Any]]:
        lab = Lab()
        data = lab.spreads(instrument, period)
        return data