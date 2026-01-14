import { Body, Controller, Get, Logger, Post } from '@nestjs/common';
import { AppService } from './app.service';
import { Ctx, EventPattern, KafkaContext, Payload } from '@nestjs/microservices';
import { map } from "rxjs";

@Controller()
export class AppController {
  private readonly logger = new Logger(AppController.name);
  constructor(private readonly appService: AppService) {}

  @Get('/api/events/health')
  public getHealth(): { status: boolean } {
    this.logger.debug('/health');
    return {
      status: true,
    };
  }

  @Post('/api/events/movie')
  public createMovieEvent(@Body() event: unknown) {
    this.logger.debug('/api/events/movie');
    return this.appService.publishMovieEvent(event).pipe(map(() => ({
      status: 'success',
    })));
  }

  @Post('/api/events/payment')
  public createPaymentEvent(@Body() event: unknown) {
    this.logger.debug('/api/events/payment');
    return this.appService.publishPaymentEvent(event).pipe(map(() => ({
      status: 'success',
    })));
  }

  @Post('/api/events/user')
  public createUserEvent(@Body() event: unknown) {
    this.logger.debug('/api/events/user');
    return this.appService.publishUserEvent(event).pipe(map(() => ({
      status: 'success',
    })));
  }

  @EventPattern('user-events')
  public async handleUserCreated(
      @Payload() message: unknown,
      @Ctx() context: KafkaContext,
  ): Promise<void> {
    this.logger.debug(`user-events: ${JSON.stringify(message)}`);
  }

  @EventPattern('movie-events')
  public async handleMovieCreated(
      @Payload() message: unknown,
      @Ctx() context: KafkaContext,
  ): Promise<void> {
    this.logger.debug(`movie-events: ${JSON.stringify(message)}`);
  }

  @EventPattern('payment-events')
  public async handlePaymentCreated(
      @Payload() message: unknown,
      @Ctx() context: KafkaContext,
  ): Promise<void> {
    this.logger.debug(`payment-events: ${JSON.stringify(message)}`);
  }
}
