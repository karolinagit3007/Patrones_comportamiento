package java.patrones; 

import java.util.List;
import java.util.Map;

abstract class OrderHandler {
    private OrderHandler nextHandler;

    public OrderHandler(OrderHandler nextHandler) {
        this.nextHandler = nextHandler;
    }

    public OrderHandler setNext(OrderHandler nextHandler) {
        this.nextHandler = nextHandler;
        return nextHandler;
    }

    public String handle(Map<String, Object> order) {
        if (nextHandler != null) {
            return nextHandler.handle(order);
        }
        return "Orden procesada con éxito.";
    }
}

class OrderValidationHandler extends OrderHandler {
    public OrderValidationHandler(OrderHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    public String handle(Map<String, Object> order) {
        if (!order.containsKey("items") || ((List<?>) order.get("items")).isEmpty()) {
            return "La orden no tiene artículos.";
        }
        System.out.println("Orden validada correctamente.");
        return super.handle(order);
    }
}

class StockCheckHandler extends OrderHandler {
    public StockCheckHandler(OrderHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    public String handle(Map<String, Object> order) {
        Object itemsObj = order.get("items");
        if (itemsObj instanceof List<?>) {
            List<?> items = (List<?>) itemsObj; 
            for (Object itemObj : items) {
                if (itemObj instanceof Map<?, ?>) {
                    Map<?, ?> item = (Map<?, ?>) itemObj;
                    if ((int) item.get("stock") <= 0) {
                        return "Uno o más artículos no están en stock.";
                    }
                }
            }
            System.out.println("Stock verificado correctamente.");
        } else {
            return "No se pudo verificar el stock.";
        }

        return super.handle(order);
    }
}

class PaymentHandler extends OrderHandler {
    public PaymentHandler(OrderHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    public String handle(Map<String, Object> order) {
        if (!(Boolean) order.getOrDefault("payment_successful", false)) {
            return "Pago no realizado correctamente.";
        }
        System.out.println("Pago procesado correctamente.");
        return super.handle(order);
    }
}

class ShippingHandler extends OrderHandler {
    public ShippingHandler(OrderHandler nextHandler) {
        super(nextHandler);
    }

    @Override
    public String handle(Map<String, Object> order) {
        if (!order.containsKey("address") || order.get("address").toString().isEmpty()) {
            return "La dirección de envío no está proporcionada.";
        }
        System.out.println("Envío programado correctamente.");
        return super.handle(order);
    }
}

public class ChainResponsability {
    public static void main(String[] args) {
        Map<String, Object> order = Map.of(
            "items", List.of(
                Map.of("name", "Laptop", "stock", 10),
                Map.of("name", "Mouse", "stock", 5)
            ),
            "payment_successful", true,
            "address", "123 Calle Ficticia, Ciudad"
        );

        OrderValidationHandler orderValidationHandler = new OrderValidationHandler(null);
        StockCheckHandler stockCheckHandler = new StockCheckHandler(null);
        PaymentHandler paymentHandler = new PaymentHandler(null);
        ShippingHandler shippingHandler = new ShippingHandler(null);

        orderValidationHandler.setNext(stockCheckHandler)
                .setNext(paymentHandler)
                .setNext(shippingHandler);

        String result = orderValidationHandler.handle(order);

        System.out.println(result);
    }
}
