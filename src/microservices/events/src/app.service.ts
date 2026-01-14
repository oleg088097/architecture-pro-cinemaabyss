import { Injectable } from '@nestjs/common';
import { Client, Transport, type ClientKafkaProxy } from "@nestjs/microservices";

@Injectable()
export class AppService {
    @Client({
        transport: Transport.KAFKA,
        options: {
            client: {
                clientId: 'events',
                brokers: process.env.KAFKA_BROKERS!.split(','),
            },
            consumer: {
                groupId: 'events-service',
            }
        }
    })
    client: ClientKafkaProxy;

    public constructor(
    ) {
    }

    public publishUserEvent(event: unknown) {
        return this.publishEvent(event, 'user-events')
    }
    public publishMovieEvent(event: unknown) {
        return this.publishEvent(event, 'movie-events')
    }
    public publishPaymentEvent(event: unknown) {
        return this.publishEvent(event, 'payment-events')
    }

    private publishEvent(event: unknown, topic: string) {
        return this.client.emit(topic, event);
    }
}
